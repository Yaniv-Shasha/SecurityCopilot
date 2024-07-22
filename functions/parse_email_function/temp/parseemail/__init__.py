import logging
import json
import re
import hashlib
import tldextract
from email import policy
from email.parser import BytesParser
from email.message import EmailMessage
from typing import List, Dict
import azure.functions as func
from urllib.parse import urlparse

def extract_domains(raw_email: bytes) -> List[str]:
    """Extracts and deduplicates domains from a raw email using tldextract."""
    logging.info("Extracting domains from raw email")
    content = raw_email.decode('utf-8', errors='ignore')
    
    # Regular expression for domain extraction
    domain_pattern = r'\b[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}\b'
    
    domains = re.findall(domain_pattern, content)
    
    # Deduplicate domains and filter invalid ones using tldextract
    valid_domains = {
        f"{extracted.domain}.{extracted.suffix}"
        for domain in set(domains)
        if (extracted := tldextract.extract(domain)).domain and extracted.suffix
    }

    return list(valid_domains)

def get_attachments(email_message: EmailMessage) -> List[Dict[str, str]]:
    """Extracts attachments from an email message and computes their SHA-256 hashes."""
    attachments = [
        {
            'attachment_name': part.get_filename(),
            'attachment_sha256': hashlib.sha256(part.get_payload(decode=True)).hexdigest()
        }
        for part in email_message.iter_attachments()
        if part.get_filename()
    ]
    return attachments

def parse_ip_and_urls(raw_email: bytes) -> Dict[str, List[str]]:
    """Parses raw email for IP addresses and URLs."""
    logging.info("Parsing raw email for IP addresses and URLs")
    content = raw_email.decode('utf-8', errors='ignore')
    
    # Regular expressions for IPv4, IPv6 and URLs
    ipv4_pattern = r'\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b'
    ipv6_pattern = r'\b(?:[a-fA-F0-9]{1,4}:){7}[a-fA-F0-9]{1,4}\b'
    url_pattern = r'https?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+(?:\>|\"|\')?'
    
    ipv4_addresses = re.findall(ipv4_pattern, content)
    ipv6_addresses = re.findall(ipv6_pattern, content)
    urls = re.findall(url_pattern, content)
    
    # Remove trailing characters from URLs
    urls = [re.sub(r'[>\'"]$', '', url) for url in urls]
    
    # Deduplicate IP addresses and URLs
    ip_addresses = list(set(ipv4_addresses + ipv6_addresses))
    filtered_urls = list({urlparse(url).netloc: url for url in urls}.values())

    return {
        'ip_addresses': ip_addresses,
        'urls': filtered_urls
    }

def parse_email(raw_email: bytes) -> List[Dict[str, str]]:
    messages = []
    current_email = raw_email

    while current_email:
        logging.info("Parsing current email chunk")
        parsed_email = BytesParser(policy=policy.default).parsebytes(current_email)

        attachments = get_attachments(parsed_email)

        message_info = {
            'from': parsed_email['from'],
            'to': parsed_email['to'],
            'date': parsed_email['date'],
            'subject': parsed_email['subject'],
            'body': get_body(parsed_email),
            'attachments': attachments
        }

        messages.append(message_info)
        logging.info(f"Parsed message: {message_info}")

        forwarded_message = extract_forwarded_message(message_info['body'])
        if forwarded_message:
            logging.info("Forwarded message found, stopping further parsing")
            break  # Stop parsing as we have extracted the forwarded message
        else:
            logging.info("No forwarded message found, stopping parse")
            break

    return messages

def get_body(email_message: EmailMessage) -> str:
    """Extracts the body from an email message."""
    if email_message.is_multipart():
        logging.info("Email is multipart, iterating over parts")
        return "\n".join(
            get_body(part)
            for part in email_message.iter_parts()
            if part.is_multipart() or part.get_content_type() == 'text/plain'
        )
    else:
        logging.info("Email is not multipart, extracting payload directly")
        return email_message.get_payload(decode=True).decode(email_message.get_content_charset() or 'utf-8')

def extract_forwarded_message(body: str) -> str:
    """Extracts the forwarded message from the body text."""
    logging.info("Checking for forwarded message in body")
    split_keywords = ["---------- Forwarded message ---------", "-----Original Message-----"]
    for keyword in split_keywords:
        if keyword in body:
            parts = body.split(keyword, 1)
            logging.info("Forwarded message keyword found, extracting forwarded content")
            # Return the part after the forwarded message keyword
            forwarded_content = parts[1].strip()
            # Strip metadata headers from the forwarded message
            forwarded_body = "\n".join(forwarded_content.split('\n')[4:]).strip()  # Assuming the first 4 lines are headers
            return forwarded_body
    logging.info("No forwarded message keyword found in body")
    return None

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    try:
        raw_email = req.get_body()  # Get raw email from the HTTP request body
        
        # Extract domains
        domains = extract_domains(raw_email)
        
        # Extract IP addresses and URLs
        ip_and_urls = parse_ip_and_urls(raw_email)
        
        # Parse email content
        parsed_messages = parse_email(raw_email)

        # Creating the JSON dictionary
        result = {
            "email_content": parsed_messages,
            "ip_addresses": ip_and_urls['ip_addresses'],
            "urls": ip_and_urls['urls'],
            "domains": domains
        }
        
        # Converting the result to a JSON string
        json_result = json.dumps(result, indent=4)
        
        # Returning the JSON string as an HTTP response
        return func.HttpResponse(json_result, mimetype="application/json")
    
    except Exception as e:
        logging.error(f"Error processing request: {e}")
        return func.HttpResponse(f"Error: {e}", status_code=500)
