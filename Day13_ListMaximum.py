import streamlit as st

# Page config
st.set_page_config(page_title="🔢 Find Largest Number", layout="centered")

# CSS for enhanced UI
st.markdown("""
    <style>
    .main-title {
        text-align: center;
        font-size: 36px;
        font-weight: bold;
        color: #2c3e50;
        margin-bottom: 30px;
    }
    .result-box {
        font-size: 28px;
        font-weight: bold;
        color: #155724;
        background-color: #d4edda;
        border-left: 6px solid #28a745;
        padding: 20px;
        border-radius: 8px;
        margin-top: 20px;
        text-align: center;
    }
    .stTextInput>div>input {
        font-size: 18px;
        height: 45px;
        padding: 8px;
        border-radius: 6px;
    }
    .stButton>button {
        font-size: 20px;
        padding: 10px 30px;
        border-radius: 6px;
        background-color: #007bff;
        color: white;
        border: none;
        transition: all 0.2s ease;
    }
    .stButton>button:hover {
        background-color: #0056b3;
        transform: scale(1.03);
    }
    </style>
""", unsafe_allow_html=True)

# Title
st.markdown("<div class='main-title'>🔍 Find the Largest Number in a List</div>", unsafe_allow_html=True)

# Input
number_input = st.text_input("Enter numbers separated by commas (e.g., 5, 22, 13, 8, 90):", placeholder="e.g., 5, 10, 22")

# Button to trigger logic
if st.button("Find Largest Number"):
    try:
        # Convert input to list of numbers
        num_list = [float(num.strip()) for num in number_input.split(",") if num.strip()]
        
        # Validate list
        if not num_list:
            st.error("Please enter at least one valid number.")
        else:
            # Find largest number manually
            largest = num_list[0]
            for num in num_list[1:]:
                if num > largest:
                    largest = num

            # Show result in enhanced box
            st.markdown(f"<div class='result-box'>✅ Largest Number: <strong>{largest}</strong></div>", unsafe_allow_html=True)
    except ValueError:
        st.error("❌ Invalid input! Please enter only numbers separated by commas.")
