import streamlit as st

st.set_page_config(page_title="Login Validator", layout="centered")

st.markdown("## 🔐 User Login Form")
st.markdown("Please enter your credentials to validate access.")
st.write("")  # spacer

# Layout with two input fields side by side
with st.form("login_form"):
    col1, col2 = st.columns(2)
    with col1:
        username = st.text_input("👤 Username", placeholder="Enter username")
    with col2:
        password = st.text_input("🔑 Password", type="password", placeholder="Min 7 characters")

    submitted = st.form_submit_button("🚀 Validate")

if submitted:
    if username.strip() == "":
        st.error("⚠️ Username cannot be empty.")
    elif len(password) < 7:
        st.error("❌ Password too short. Must be at least 7 characters.")
    else:
        st.success(f"✅ Welcome, **{username}**! Your credentials are valid.")
