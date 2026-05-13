import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import os
from dotenv import load_dotenv
from twilio.rest import Client
load_dotenv()
print(os.environ.get("TWILIO_ACCOUNT_SID"))  # None çıxırsa problem .env-dədir


load_dotenv()

def send_sms(phone_number, message):
    account_sid = os.environ.get("TWILIO_ACCOUNT_SID")
    auth_token = os.environ.get("TWILIO_AUTH_TOKEN")
    from_number = os.environ.get("TWILIO_FROM_NUMBER")

    client = Client(account_sid, auth_token)
    msg = client.messages.create (
        body=message,
        from_=from_number,
        to=phone_number
    )

    print(f'SMS göndərildi! SID: {msg.sid}')
    return True