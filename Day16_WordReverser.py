import streamlit as st

st.set_page_config(page_title="Reverse Words", layout="centered")
st.title("🔁 Reverse Each Word in a Sentence")

# Input box
sentence = st.text_input("Enter a sentence to reverse each word:")

# Process and display
if sentence:
    reversed_words = " ".join([word[::-1] for word in sentence.split()])
    st.markdown("### 🔄 Reversed Sentence:")
    st.success(reversed_words)
