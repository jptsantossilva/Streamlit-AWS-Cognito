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

def main():
    st.write(
        """
        This shows that you have access to the page. Enjoy!
        """
    )

st.header("Page 2")

# if user logged in and belongs to group group2
if st.session_state["authenticated"] and "group2" in st.session_state["user_cognito_groups"]:
    main()
else:
    if st.session_state["authenticated"]:
        st.write("You do not have access to this page.")
    else:
        st.write("Please login!")

