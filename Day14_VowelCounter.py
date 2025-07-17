import streamlit as st
from collections import Counter

# Page configuration
st.set_page_config(page_title="🗣️ Vowel Counter", layout="centered")

# CSS styling
st.markdown("""
    <style>
    .header {
        text-align: center;
        font-size: 36px;
        font-weight: bold;
        color: #2c3e50;
        margin-bottom: 30px;
    }
    .result-box {
        font-size: 20px;
        font-weight: bold;
        color: #0c5460;
        background-color: #d1ecf1;
        border-left: 6px solid #17a2b8;
        padding: 20px;
        border-radius: 8px;
        margin-top: 20px;
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
        background-color: #28a745;
        color: white;
        border: none;
        transition: all 0.2s ease;
    }
    .stButton>button:hover {
        background-color: #1e7e34;
        transform: scale(1.03);
    }
    ul {
        padding-left: 20px;
    }
    </style>
""", unsafe_allow_html=True)

# Header
st.markdown("<div class='header'>🔡 Vowel Counter</div>", unsafe_allow_html=True)

# Input
word = st.text_input("Enter a word:", placeholder="e.g., Streamlit")

# Button
if st.button("Count Vowels"):
    if not word:
        st.warning("⚠️ Please enter a word.")
    else:
        word_lower = word.lower()
        vowels = 'aeiou'
        vowel_counts = Counter(char for char in word_lower if char in vowels)
        total_vowels = sum(vowel_counts.values())

        # Display result
        result_html = f"<div class='result-box'>"
        result_html += f"🔢 <strong>Total vowels in '{word}':</strong> {total_vowels}<br><br>"
        result_html += "<ul>"
        for v in vowels:
            result_html += f"<li><strong>{v.upper()}</strong>: {vowel_counts.get(v, 0)}</li>"
        result_html += "</ul></div>"

        st.markdown(result_html, unsafe_allow_html=True)
