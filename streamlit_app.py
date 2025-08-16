import streamlit as st

# --- st.title("DevOps Calculator"); ---

about_page = st.Page(
    page="pages/about_me.py",
    title="About Me",
    default=True,
)

project_1_page = st.Page(
    page="pages/sales_dashboard.py",
    title="Sales Dashboard",
)

project_2_page = st.Page(
    page="pages/chatbot.py",
    title="Chat Bot",
)

project_3_page = st.Page(
    page="pages/devops_calculator.py",
    title="The DevOps Calculator",
)

# --- Navigation menu ---
# --- pg = st.navigation(pages=[about_page, project_1_page, project_2_page, project_3_page]) ---


# --- navigation setup with sections ---
pg = st.navigation(
    {
        "Info": [about_page],
        "Projects": [project_1_page, project_2_page, project_3_page],
    }
)

# --- Run Navigation ---
pg.run()
