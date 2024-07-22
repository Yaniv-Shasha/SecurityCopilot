import logging
import json
import hashlib
import re
from email import policy
from email.parser import BytesParser
from bs4 import BeautifulSoup
from urllib.parse import urlparse
import azure.functions as func

# Configure logging
logger = logging.getLogger(__name__)
'''
def extract_urls_from_text(email_text):
    url_pattern = re.compile(r'https?://[\w./?&=-]+')
    urls = url_pattern.findall(email_text)
    return urls

def get_base_urls(urls):
    base_urls = set()
    for url in urls:
        parsed_url = urlparse(url)
        base_url = f"{parsed_url.scheme}://{parsed_url.netloc}"
        base_urls.add(base_url)
    return list(base_urls)

def strip_html_tags(text):
    soup = BeautifulSoup(text, "html.parser")
    for br in soup.find_all("br"):
        br.decompose()
    text = soup.get_text(separator='\n').strip()
    return text

def clean_newlines(text):
    return re.sub(r'\n+', '\n', text)

def extract_ip_addresses(text):
    ip_pattern = re.compile(r'\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b|\b(?:[a-fA-F0-9]{1,4}:){7}[a-fA-F0-9]{1,4}\b')
    ips = ip_pattern.findall(text)
    return ips

def parse_domains_from_urls(urls):
    domains = set()
    for url in urls:
        parsed_url = urlparse(url)
        domain = parsed_url.netloc
        domains.add(domain)
    return list(domains)

def get_email_body(msg):
    plain_text_body = ""
    html_body = ""#

    if msg.is_multipart():
        for part in msg.walk():
            content_type = part.get_content_type()
            content_disposition = part.get("Content-Disposition", None)
            if content_type == 'text/plain' and content_disposition != 'attachment':
                plain_text_body = part.get_payload(decode=True).decode(part.get_content_charset() or 'utf-8')
            elif content_type == 'text/html' and content_disposition != 'attachment':
                html_body = part.get_payload(decode=True).decode(part.get_content_charset() or 'utf-8')
    else:
        content_type = msg.get_content_type()
        if content_type == 'text/plain':
            plain_text_body = msg.get_payload(decode=True).decode(msg.get_content_charset() or 'utf-8')
        elif content_type == 'text/html':
            html_body = msg.get_payload(decode=True).decode(msg.get_content_charset() or 'utf-8')

    return plain_text_body, html_body
'''
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

def parse_eml(email_content):
    try:
        msg = BytesParser(policy=policy.default).parsebytes(email_content)
        logger.info(f"Parsed email message: {msg}")

        sender = msg.get('From', '')
        #sender_domain = sender.split('@')[-1] if '@' in sender else ''
        return_path = msg.get('Return-Path', '')
        receiver = msg.get('To', '')
        subject = msg.get('Subject', '')
        reply_to = msg.get('Reply-To', '')

        #plain_text_body, html_body = get_email_body(msg)
        #logger.info(f"Plain text body: {plain_text_body}")
        #logger.info(f"HTML body: {html_body}")

        #urls = extract_urls_from_text(plain_text_body) + extract_urls_from_text(html_body)
        #base_urls = get_base_urls(urls)
        #logger.info(f"Extracted URLs: {urls}")
        #logger.info(f"Base URLs: {base_urls}")

        #ip_addresses = extract_ip_addresses(plain_text_body) + extract_ip_addresses(html_body)
        #for received_header in msg.get_all('Received', []):
        #    ip_addresses.extend(extract_ip_addresses(received_header))
        #ip_addresses = list(set(ip_addresses))
        #logger.info(f"Extracted IP addresses: {ip_addresses}")

        #domains = parse_domains_from_urls(urls)
        #if sender_domain:
        #    domains.append(sender_domain)
        #logger.info(f"Extracted domains: {domains}")

        #body_text = strip_html_tags(html_body)
        #body_text = clean_newlines(body_text)
        #logger.info(f"Cleaned body text: {body_text}")

        #attachment_hash = ""
        #attachment_name = ""
        #if msg.is_multipart():
        #    for part in msg.iter_attachments():
        #        attachment_name = part.get_filename()
        #        if attachment_name:
        #            attachment_data = part.get_payload(decode=True)
        #            attachment_hash = hashlib.sha256(attachment_data).hexdigest()
        #            break
        #logger.info(f"Attachment name: {attachment_name}, hash: {attachment_hash}")

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
            "delivered_to": msg.get('Delivered-To', ''),
            "received": msg.get_all('Received', [])
        }

        email_data = {
            "sender": sender,
            "return_path": return_path,
            "receiver": receiver,
            "reply_to": reply_to,
            "subject": subject,
            #"attachment_hash": attachment_hash,
            #"attachment_name": attachment_name,
            #"body": body_text,
            #"urls": base_urls,
            #"ipaddresses": ip_addresses,
            #"domains": domains,
            "smtp": smtp,
            "dkim_result": dkim_result,
            "spf_result": spf_result,
            "dmarc_result": dmarc_result
        }
        logger.info(f"Final parsed email data: {email_data}")

        return email_data
    except Exception as e:
        logger.error(f"Error parsing email: {str(e)}")
        return None

def main(req: func.HttpRequest) -> func.HttpResponse:
    logger.info('Python HTTP trigger function processed a request.')

    try:
        raw_body = req.get_body().decode('utf-8')
        logger.info(f"Received email content: {raw_body[:500]}")  # Log first 500 bytes of email content

        parsed_email = parse_eml(raw_body.encode())
        if parsed_email is None:
            logger.error("Failed to parse email.")
            return func.HttpResponse(
                "Failed to parse email.",
                status_code=500
            )

        logger.info(f"Parsed email data: {json.dumps(parsed_email, indent=4)}")  # Log parsed email data

        return func.HttpResponse(f"{json.dumps(parsed_email, indent=4)}", status_code=200)
    except Exception as e:
        logging.error(f"Error processing request: {str(e)}")
        return func.HttpResponse(f"Error processing request: {str(e)}", status_code=400)
