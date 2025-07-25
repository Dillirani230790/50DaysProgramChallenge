import streamlit as st

st.set_page_config(page_title="Phone Number Formatter", layout="centered")
st.title("📞 Phone Number Formatter")

# Initialize session state only once
if "phone_input" not in st.session_state:
    st.session_state.phone_input = ""
if "formatted_number" not in st.session_state:
    st.session_state.formatted_number = ""

# Function to format phone number
def format_phone_number():
    number = ''.join(filter(str.isdigit, str(st.session_state.phone_input)))
    if len(number) != 10:
        st.session_state.formatted_number = "❌ Invalid input. Enter exactly 10 digits."
    else:
        st.session_state.formatted_number = f"✅ Formatted Number: ({number[:3]}) {number[3:6]}-{number[6:]}"


# Function to clear input and result
def clear_input():
    st.session_state.phone_input = ""
    st.session_state.formatted_number = ""


# Input field
st.text_input("Enter a 10-digit phone number", key="phone_input")

# Buttons
col1, col2 = st.columns(2)
with col1:
    st.button("Format Number", on_click=format_phone_number)

with col2:
    st.button("Clear", on_click=clear_input)

# Display result
if st.session_state.formatted_number:
    st.markdown(f"### {st.session_state.formatted_number}")
