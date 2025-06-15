# Utility for parsing emails and extracting lead data
import re
from googleapiclient.discovery import build
from google.oauth2.credentials import Credentials

def parse_email(email_data):
    # Parse email data and extract lead information
    # Note: This is a simplified example using Gmail API
    try:
        # Assume email_data is fetched via Gmail API
        headers = email_data['payload']['headers']
        body = email_data.get('snippet', '')  # Simplified body extraction

        # Extract sender email and name
        from_header = next(h['value'] for h in headers if h['name'] == 'From')
        email_match = re.search(r'<(.+?)>', from_header) or re.search(r'(\S+@\S+)', from_header)
        email = email_match.group(1) if email_match else ''
        name = from_header.split('<')[0].strip() if '<' in from_header else ''

        # Split name into first and last (simplified)
        name_parts = name.split()
        first_name = name_parts[0] if name_parts else ''
        last_name = ' '.join(name_parts[1:]) if len(name_parts) > 1 else ''

        # Extract phone number from body (simplified regex)
        phone_match = re.search(r'\b\d{10}\b', body)
        phone = phone_match.group(0) if phone_match else ''

        # Extract company (heuristic: look for common patterns)
        company_match = re.search(r'(?:company|organization):?\s*(\w+)', body, re.IGNORECASE)
        company = company_match.group(1) if company_match else ''

        # Return lead data
        return {
            'first_name': first_name,
            'last_name': last_name,
            'email': email,
            'phone': phone,
            'company': company,
            'message': body[:1000],  # Truncate body for storage
        }
    except Exception as e:
        # Log error for debugging
        print(f"Error parsing email: {e}")
        return None