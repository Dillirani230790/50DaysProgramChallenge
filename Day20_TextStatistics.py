import streamlit as st

st.set_page_config(page_title="Text Analyzer", layout="centered")

st.title("📝 Paragraph Analyzer")

st.markdown("Enter a paragraph below to get the total **word**, **sentence**, and **character** count.")
paragraph = st.text_area("Enter your paragraph here", height=200)

# Functions
def count_words(text):
    return len(text.split())

def count_sentences(text):
    # Split on '.' and remove empty strings
    sentences = [s for s in text.split('.') if s.strip()]
    return len(sentences)

def count_characters(text):
    return len(text)

# Analyze button
if st.button("Analyze"):
    if paragraph.strip() == "":
        st.warning("Please enter some text.")
    else:
        words = count_words(paragraph)
        sentences = count_sentences(paragraph)
        characters = count_characters(paragraph)

        st.markdown("### 📊 Results:")
        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric("🧾 Words", words)

        with col2:
            st.metric("📘 Sentences", sentences)

        with col3:
            st.metric("🔠 Characters", characters)

        st.success("Analysis complete! 🎉")

# Clear button
if st.button("Clear"):
    st.rerun()
