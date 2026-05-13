import os
from dotenv import load_dotenv

# .env faylının tam yolunu göstər
load_dotenv(r"C:\Users\user\Desktop\load-agent\.env")

from src.sms_client import send_sms

send_sms(
    phone_number="+994773010976",
    message="Test SMS! Agent işləyir 🚛"
)