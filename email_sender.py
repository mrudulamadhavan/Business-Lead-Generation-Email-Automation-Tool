import base64
from email.mime.text import MIMEText
from googleapiclient.discovery import build
from google.oauth2.credentials import Credentials
import gspread
from oauth2client.service_account import ServiceAccountCredentials

def send_email(to, subject, message_text):
    creds = Credentials.from_authorized_user_file("token.json", ['https://www.googleapis.com/auth/gmail.send'])
    service = build('gmail', 'v1', credentials=creds)

    message = MIMEText(message_text)
    message['to'] = to
    message['subject'] = subject

    raw = base64.urlsafe_b64encode(message.as_bytes()).decode()
    body = {'raw': raw}

    try:
        message = service.users().messages().send(userId="me", body=body).execute()
        return True
    except Exception as e:
        print("Error:", e)
        return False
