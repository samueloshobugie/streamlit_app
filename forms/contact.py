import streamlit as st
import re
import requests


WEBHOOK_URL = ""

def is_valid_email(email):
    # ---basic regex pattern for email validation ---
    email_pattern = r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$"
    return re.match(email_pattern, email) is not None



def contact_form():
    with st.form("contact_form"):
        name = st.text_input("first name")
        email = st.text_input("email address")
        message = st.text_area("your message")
        submit_button = st.form_submit_button("submit")

        if submit_button:
#           st.success("message sent")

            if not WEBHOOK_URL:
                st.error(
                    "email service is not setup"
                )
                st.stop()

            if not name:
                st.error("please provide name")
                st.stop()

            if not email: 
                st.error("please provide your email address")
                st.stop()

            if not is_valid_email(email):
                st.error("please provide a valid email address")
                st.stop()

            if not message:
                st.error("please provide a message")
                st.stop()

            # --- prepare data payload for webhook ---
            data = {"email": email, "name": name, "message": message}
            response = requests.post(WEBHOOK_URL, json=data)

            if response.status_code == 200:
                st.success("your message has been sent successfully")
            else:
                st.error("error sending message")