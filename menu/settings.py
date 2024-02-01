import streamlit as st

import components.authenticate as authenticate

# Check authentication when user lands on the page.
authenticate.set_st_state_vars()

# st.session_state

# Add login/logout buttons
if st.session_state["authenticated"]:
    authenticate.button_logout()
else:
    authenticate.button_login()

st.header("Settings")

# if user logged in and belongs to admin group
if st.session_state["authenticated"] and "admin" in st.session_state["user_cognito_groups"]:
    # Show the below Streamlit code
    st.write(
        """
        This shows that you have access to the page. Enjoy!
        """
    )

    # ...
else:
    if st.session_state["authenticated"]:
        st.write("You do not have access. Please contact the administrator.")
    else:
        st.write("Please login!")