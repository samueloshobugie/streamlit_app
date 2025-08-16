import streamlit as st

st.title("The DevOps Calculator")
st.write("Welcome! Use the sidebar to navigate between pages.")

# Example: Simple uptime calculator
uptime = st.number_input("Enter uptime percentage", min_value=0.0, max_value=100.0, value=99.9)
downtime = (100 - uptime) * 365 * 24 * 60 / 100  # minutes per year

st.write(f"Expected downtime per year: **{downtime:.2f} minutes**")