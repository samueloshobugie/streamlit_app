import streamlit as st

from forms.contact import contact_form

 

@st.dialog("contact me")
def show_contact_form():
    contact_form()

# --- hero section ---
col1, col2 = st.columns(2, gap="small", vertical_alignment="center")
with col1:
    st.image("./assets/runnaira_logo.png", width=230)
with col2:
    st.title("Samuel Oshobugie", anchor=False)
    st.write(
        "Senior DevOps Engineer and Agentic AI Automation Expert."
    )
    if st.button("Contact Me"):
        show_contact_form()

# --- experience ---
st.write("\n")
st.subheader("experience and qualification", anchor=False)
st.write(
    "7 years" \
    "strong hands on" \
    "excellent team player" 
)

# --- skills ---

st.write("\n")
st.subheader("hard skills", anchor=False)
st.write(
    "python" \
    "javascript" \
    "devops" \
    "ai agent automation" 
)