import streamlit as st

def shift_letters(text):
    result = ''
    for char in text:
        if char.isalpha():
            base = ord('a') if char.islower() else ord('A')
            shifted = chr((ord(char) - base + 1) % 26 + base)
            result += shifted
        else:
            result += char
    return result

# Streamlit UI
st.set_page_config(page_title="Shift Letters", layout="centered")
st.title("🔤 Shift Letters by 1")

# Input
user_input = st.text_input("Enter text to shift:")

# Output
if user_input:
    shifted = shift_letters(user_input)
    st.markdown("### 🔁 Shifted Result:")
    st.success(shifted)
