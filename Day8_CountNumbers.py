import streamlit as st

st.set_page_config(page_title="🔢 Number Analyzer", layout="centered")
st.title("🔍 Number Analyzer")
st.markdown("Enter a list of numbers to count how many are positive, negative, or zero.")
st.write("✏️ Enter numbers (comma-separated below):")

# User input
input_numbers = st.text_area("", placeholder="e.g. 5, -3, 0, 7, -1, 0", height=100)

# Analyze when button is pressed
if st.button("📊 Analyze"):
    if input_numbers.strip() == "":
        st.warning("⚠️ Please enter some numbers first.")
    else:
        try:
            # Convert to list of integers
            numbers = [int(x.strip()) for x in input_numbers.split(',')]

            # Count values
            positives = sum(1 for n in numbers if n > 0)
            negatives = sum(1 for n in numbers if n < 0)
            zeros = sum(1 for n in numbers if n == 0)

            # Display results
            st.success("✅ Analysis Complete!")
            st.write("### 📈 Results Summary")
            col1, col2, col3 = st.columns(3)
            col1.metric("🔵 Positive", positives)
            col2.metric("🔴 Negative", negatives)
            col3.metric("🟡 Zeros", zeros)

            st.write("#### 🔁 Input List")
            st.code(numbers)

        except ValueError:
            st.error("❌ Invalid input. Please enter only integers separated by commas.")
