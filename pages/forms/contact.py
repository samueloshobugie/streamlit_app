import streamlit as st

def contact_form():
    with st.form("contact_form"):
        name = st.text_input("first name")
        email = st.text_input("email address")
        message = st.text_area("your message")
        submit_button = st.form_submit_button("submit")

        if submit_button:
            st.success("Message successfully sent!")