import streamlit as st

st.set_page_config(page_title="Number Comparison Tool", layout="centered")
st.title("🔍 Number Comparison Tool")

# Function to safely convert text to integer
def safe_int(value):
    try:
        return int(value)
    except:
        return None

# Input fields using text to allow blank initial state
col1, col2 = st.columns(2)
with col1:
    num1 = st.text_input("🔢 Enter First Number", placeholder="e.g. 10")
with col2:
    num2 = st.text_input("🔢 Enter Second Number", placeholder="e.g. 20")

# Compare when button is clicked
if st.button("Compare"):
    n1 = safe_int(num1)
    n2 = safe_int(num2)

    if n1 is None or n2 is None:
        st.error("⚠️ Please enter valid whole numbers in both fields.")
    elif n1 > n2:
        st.success(f"✅ **{n1} is greater than {n2}.**\n\n📈 `{n1} > {n2}`")
    elif n1 < n2:
        st.info(f"🔽 **{n1} is less than {n2}.**\n\n📉 `{n1} < {n2}`")
    else:
        st.warning(f"⚖️ **Both numbers are equal: {n1} = {n2}.**")
        

