import streamlit as st

st.title("Email Username Extractor")

# Initialize session state for input
if "email" not in st.session_state:
    st.session_state.email = ""

# Text input with session state binding
st.session_state.email = st.text_input("Enter your email address", value=st.session_state.email)

# Function to extract username
def extract_username(email):
    if "@" in email and email.count("@") == 1:
        return email.split("@")[0]
    return None

col1, col2 = st.columns(2)

# Extract button
with col1:
    if st.button("Extract Username"):
        if st.session_state.email:
            username = extract_username(st.session_state.email)
            if username:
                st.success(f"Username: **{username}**")
            else:
                st.error("Invalid email format. Please enter a valid email.")
        else:
            st.warning("Please enter an email address.")

# Clear button
with col2:
    if st.button("Clear"):
        st.session_state.email = ""
        st.rerun()
