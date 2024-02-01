import streamlit as st

import components.authenticate as authenticate

st.set_page_config(
    page_title="Home",
    page_icon="👋",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Check authentication when user lands on the home page.
authenticate.set_st_state_vars()

# Add login/logout buttons
if st.session_state["authenticated"]:
    authenticate.button_logout()
else:
    authenticate.button_login()

# st.session_state

# with st.echo("below"):
from st_pages import add_page_title, show_pages, Page

show_pages(
    [
        Page("app.py", "Home"),
        Page("menu/page_2.py", "Page 2"),
        Page("menu/page_3.py", "Page 3"),
        Page("menu/settings.py", "Settings"),
    ]
)

add_page_title()  # Optional method to add title and icon to current page
# Also calls add_indentation() by default, which indents pages within a section

st.write("""
         Welcome,
         
         This app is an example of how to get User Authentication and page wise authorization in a Streamlit multi-page app using AWS Cognito 🚀! 
         """)





