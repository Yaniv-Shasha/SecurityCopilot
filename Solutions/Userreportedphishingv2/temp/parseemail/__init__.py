import logging
import json
import re
import hashlib
import tldextract
import ipaddress
from email import policy
from email.parser import BytesParser
from email.message import EmailMessage
from typing import List, Dict
import azure.functions as func
from urllib.parse import urlparse
from bs4 import BeautifulSoup

# Configure logging
logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

def parse_authentication_results(headers, keyword):
    results = []
    for header in headers:
        parts = header.split(";")
        for part in parts:
            if keyword in part:
                results.append(part.strip())
    return "; ".join(results) if results else "none"

def parse_spf(headers):
    results = []
    for header in headers:
        if header.startswith("Received-SPF"):
            results.append(header.strip())
    return "; ".join(results) if results else "none"

def extract_original_email(raw_email: bytes) -> str:
    msg = BytesParser(policy=policy.default).parsebytes(raw_email)

    original_email = None
    found_rfc822 = False

    # Extract email parts
    for part in msg.walk():
        content_type = part.get_content_type()
        main_content_type = part.get_content_maintype()
        content_disposition = part.get("Content-Disposition", None)

        if main_content_type == 'multipart':
            continue
        elif content_type == "message/rfc822" and "attachment" in content_disposition:
            found_rfc822 = True
            logging.info("Raw MSG extracted.")
            original_email = part.get_payload(0)

    if found_rfc822 and original_email:
        return original_email.as_string()
    else:
        logging.info("No MSG attachment found.")
        return raw_email.decode('utf-8', errors='ignore')

def extract_domains(content: str) -> List[str]:
    logging.info("Extracting domains from email content")

    # Pattern to extract domains and URLs
    domain_pattern = r'\b[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}\b'
    url_pattern = r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'

    # Find all URLs first
    urls = re.findall(url_pattern, content)

    # Parse domains from URLs
    url_domains = {urlparse(url).netloc for url in urls}

    # Find all domain patterns directly
    direct_domains = re.findall(domain_pattern, content)

    # Combine and clean up
    all_domains = url_domains.union(direct_domains)

    valid_domains = {
        f"{extracted.domain}.{extracted.suffix}"
        for domain in all_domains
        if (extracted := tldextract.extract(domain)).domain and extracted.suffix
    }

    return list(valid_domains)

def get_attachments(email_message: EmailMessage) -> List[Dict[str, str]]:
    attachments = [
        {
            'attachment_name': part.get_filename(),
            'attachment_sha256': hashlib.sha256(part.get_payload(decode=True)).hexdigest()
        }
        for part in email_message.iter_attachments()
        if part.get_filename()
    ]
    return attachments

def is_public_ip(ip: str) -> bool:
    try:
        ip_obj = ipaddress.ip_address(ip)
        return not (ip_obj.is_private or ip_obj.is_multicast or ip_obj.is_reserved or ip_obj.is_loopback or ip_obj.is_link_local or ip_obj.is_unspecified or ip == '255.255.255.255')
    except ValueError:
        return False

def parse_ip_and_urls(content: str) -> Dict[str, List[str]]:
    logging.info("Parsing email content for IP addresses and URLs")

    ipv4_pattern = r'\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b'
    ipv6_pattern = r'\b(?:[a-fA-F0-9]{1,4}:){7}[a-fA-F0-9]{1,4}\b|\b(?:[a-fA-F0-9]{1,4}:){1,7}:|\b(?:[a-fA-F0-9]{1,4}:){1,6}:[a-fA-F0-9]{1,4}|\b(?:[a-fA-F0-9]{1,4}:){1,5}(?::[a-fA-F0-9]{1,4}){1,2}|\b(?:[a-fA-F0-9]{1,4}:){1,4}(?::[a-fA-F0-9]{1,4}){1,3}|\b(?:[a-fA-F0-9]{1,4}:){1,3}(?::[a-fA-F0-9]{1,4}){1,4}|\b(?:[a-fA-F0-9]{1,4}:){1,2}(?::[a-fA-F0-9]{1,4}){1,5}|\b[a-fA-F0-9]{1,4}:(?:(?::[a-fA-F0-9]{1,4}){1,6})|\b:(?:(?::[a-fA-F0-9]{1,4}){1,7}|:)|\b(?:[a-fA-F0-9]{1,4}:){1,7}:|\b(?:[a-fA-F0-9]{1,4}:){6}:(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b'
    ipv4_addresses = re.findall(ipv4_pattern, content)
    ipv6_addresses = re.findall(ipv6_pattern, content)
    
    url_pattern = re.compile(
        r'http[s]?://' 
        r'(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|' 
        r'(?:%[0-9a-fA-F][0-9a-fA-F]))+'
    )
    
    valid_urls = url_pattern.findall(content)
    
    ip_addresses = list(set(ipv4_addresses + ipv6_addresses))
    filtered_ip_addresses = [ip for ip in ip_addresses if is_public_ip(ip)]
    filtered_urls = list(set(valid_urls))

    return {
        'ip_addresses': filtered_ip_addresses,
        'urls': filtered_urls
    }


def get_body(email_message: EmailMessage) -> str:
    if email_message.is_multipart():
        logging.info("Email is multipart, iterating over parts")
        parts = [
            get_body(part).strip()
            for part in email_message.iter_parts()
            if part.is_multipart() or part.get_content_type() in ['text/plain', 'text/html']
        ]
        return "\n".join(part for part in parts if part)
    else:
        logging.info("Email is not multipart, extracting payload directly")
        payload = email_message.get_payload(decode=True)
        charset = email_message.get_content_charset() or 'utf-8'
        return payload.decode(charset).strip() if payload else ""


def strip_html_tags(text: str) -> str:
    return BeautifulSoup(text, "html.parser").get_text()

def extract_forwarded_message(body: str) -> str:
    logging.info("Checking for forwarded message in body")
    split_keywords = ["---------- Forwarded message ---------", "-----Original Message-----"]
    for keyword in split_keywords:
        if keyword in body:
            parts = body.split(keyword, 1)
            logging.info("Forwarded message keyword found, extracting forwarded content")
            forwarded_content = parts[1].strip()
            forwarded_body = "\n".join(forwarded_content.split('\n')[4:]).strip()
            return forwarded_body
    logging.info("No forwarded message keyword found in body")
    return None

def parse_email(raw_email: bytes) -> Dict:
    try:
        msg = BytesParser(policy=policy.default).parsebytes(raw_email)

        sender = msg.get('From', '') or ""
        return_path = msg.get('Return-Path', '') or ""
        receiver = msg.get('To', '') or ""
        subject = msg.get('Subject', '') or ""
        reply_to = msg.get('Reply-To', '') or ""
        date = msg.get('Date', '') or ""
        body = get_body(msg)
    
        # Extract forwarded message if present
        forwarded_body = extract_forwarded_message(body)
        if forwarded_body:
            logging.info("Forwarded message found and extracted")
            body = forwarded_body
        else:
            logging.info("No forwarded message found")

        dkim_result = parse_authentication_results(msg.get_all('ARC-Authentication-Results', []), "dkim=")
        if dkim_result == "none":
            dkim_result = parse_authentication_results(msg.get_all('Authentication-Results', []), "dkim=")

        spf_result = parse_spf(msg.get_all('Received-SPF', []))
        if spf_result == "none":
            spf_result = parse_authentication_results(msg.get_all('Authentication-Results', []), "spf=")

        dmarc_result = parse_authentication_results(msg.get_all('ARC-Authentication-Results', []), "dmarc=")
        if dmarc_result == "none":
            dmarc_result = parse_authentication_results(msg.get_all('Authentication-Results', []), "dmarc=")

        smtp = {
            "delivered_to": msg.get('Delivered-To', '') or "",
            "received": msg.get_all('Received', []) or []
        }

        attachments = get_attachments(msg)

        email_data = {
            "sender": sender,
            "return_path": return_path,
            "receiver": receiver,
            "reply_to": reply_to,
            "subject": subject,
            "date": date,
            "smtp": smtp,
            "dkim_result": dkim_result,
            "spf_result": spf_result,
            "dmarc_result": dmarc_result,
            "body": strip_html_tags(body),
            "attachments": attachments,
        }

        return email_data
    except Exception as e:
        logger.error(f"Error parsing email: {str(e)}")
        return None

def recursive_parse(content):
    all_domains = set()
    all_ip_addresses = set()
    all_urls = set()
    
    if isinstance(content, dict):
        for key, value in content.items():
            domains, ips, urls = recursive_parse(value)
            all_domains.update(domains)
            all_ip_addresses.update(ips)
            all_urls.update(urls)
    elif isinstance(content, list):
        for item in content:
            domains, ips, urls = recursive_parse(item)
            all_domains.update(domains)
            all_ip_addresses.update(ips)
            all_urls.update(urls)
    elif isinstance(content, str):
        all_domains.update(extract_domains(content))
        ip_and_urls = parse_ip_and_urls(content)
        all_ip_addresses.update(ip_and_urls['ip_addresses'])
        all_urls.update(ip_and_urls['urls'])
    
    return all_domains, all_ip_addresses, all_urls

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    try:
        raw_email = req.get_body()

        # Check if the raw email is a string, if so, convert it to bytes
        if isinstance(raw_email, str):
            raw_email = raw_email.encode('utf-8')

        original_email = extract_original_email(raw_email)
        parsed_email_data = parse_email(original_email.encode())

        if parsed_email_data:
            all_domains, all_ip_addresses, all_urls = recursive_parse(parsed_email_data)

            result = {
                "email_content": parsed_email_data,
                "ip_addresses": list(all_ip_addresses),
                "urls": list(all_urls),
                "domains": list(all_domains),
            }

            json_result = json.dumps(result, indent=4)
            return func.HttpResponse(json_result, mimetype="application/json")
        else:
            logging.error("Failed to parse email.")
            return func.HttpResponse("Failed to parse email.", status_code=400)
    
    except Exception as e:
        logging.error(f"Error processing request: {e}")
        return func.HttpResponse(f"Error: {e}", status_code=500)