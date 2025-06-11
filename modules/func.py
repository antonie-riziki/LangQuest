import string
import random
import secrets
import re
import os
import africastalking
import streamlit as st 
import google.generativeai as genai


from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key = os.getenv("GOOGLE_API_KEY"))

africastalking.initialize(
    username='EMID',
    api_key = os.getenv("AT_API_KEY")
)

sms = africastalking.SMS
airtime = africastalking.Airtime
voice = africastalking.Voice

def send_sms(phone_number, otp_sms):
    # amount = "10"
    # currency_code = "KES"

    recipients = [f"+254{str(phone_number)}"]

    # airtime_rec = "+254" + str(phone_number)

    print(recipients)
    print(phone_number)

    # Set your message
    message = f"{otp_sms}";

    # Set your shortCode or senderId
    sender = 20880

    try:
        # responses = airtime.send(phone_number=airtime_rec, amount=amount, currency_code=currency_code)
        response = sms.send(message, recipients, sender)

        print(response)

        # print(responses)

    except Exception as e:
        print(f'Houston, we have a problem: {e}')

    st.toast(f"OTP Sent Successfully")


def welcome_message(first_name, phone_number, site_id):

    recipients = [f"+254{str(phone_number)}"]

    print(recipients)
    print(phone_number)

    # Set your message
    message = f"Greetings {first_name}, welcome to our site. Lets build together. Remember to stay safe. Incase of emergency call 07xxxxxxx \nSite ID: {site_id}";

    # Set your shortCode or senderId
    sender = 20880

    try:
        response = sms.send(message, recipients, sender)

        print(response)

    except Exception as e:
        print(f'Houston, we have a problem: {e}')

    st.toast(f"Account Created Successfully")



def make_call(phone_number):    
  
  # Set your Africa's Talking phone number in international format
    callFrom = "+254730731123"
  
  # Set the numbers you want to call to in a comma-separated list
    callTo   = [f"+254{str(phone_number)}"]
    
    try:
  # Make the call
        result = voice.call(callFrom, callTo)
        print (result)
    except Exception as e:
        print ("Encountered an error while making the call:%s" %str(e))



def generate_otp(length=6):
    characters = string.ascii_uppercase + string.digits
    return ''.join(secrets.choice(characters) for _ in range(length))



def check_and_encrypt_password(password: str, confirm_password: str):
    
    if password != confirm_password:
        return st.error("Error: Passwords do not match!")

    if len(password) < 8:
        return st.error(f"Error: Password must be at least 8 characters long!")
    
    if not re.search(r"[A-Z]", password):
        return st.error(f"Error: Password must contain at least one uppercase letter!")
    
    if not re.search(r"\d", password):
        return st.error(f"Error: Password must contain at least one number!")
    
    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        return st.error(f"Error: Password must contain at least one special character!")

    # Encrypt password using bcrypt
    hashed_password = bcrypt.hashpw(password.encode(), bcrypt.gensalt())

    return st.text_input(label='Encrypted password', value=hashed_password.decode(), type='password')


