import streamlit as st

st.title("Age Category Checker")

# Input age
age = st.number_input("Enter age", min_value=0, max_value=120, step=1)

# Check button
if st.button("Check Category"):
    if age <= 12:
        st.success("This person is a **Child**.")
    elif age <= 19:
        st.info("This person is a **Teenager**.")
    elif age <= 59:
        st.warning("This person is an **Adult**.")
    else:
        st.error("This person is a **Senior**.")
