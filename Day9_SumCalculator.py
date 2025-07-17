import streamlit as st

# Set page config
st.set_page_config(page_title="Sum Calculator", layout="centered")

# Custom CSS styling
st.markdown("""
<style>
    .main-title {
        font-size: 2.5rem;
        color: #004488;
        font-weight: bold;
        margin-bottom: 0.5rem;
    }
    .desc-text {
        font-size: 1.1rem;
        color: #333;
        margin-bottom: 1.5rem;
    }
    .input-container {
        display: flex;
        align-items: center;
        gap: 8px;
        margin-bottom: 20px;
    }
    .input-label {
        font-weight: 500;
        white-space: nowrap;
    }
    div[data-testid="stNumberInput"] {
        width: 160px !important;
        margin: 0 !important;
    }
    div[data-testid="stNumberInput"] input {
        text-align: center;
        font-size: 1rem;
    }
    .result-box {
        background-color: #e8f4ff;
        padding: 1rem;
        border-left: 6px solid #1f77b4;
        border-radius: 8px;
        margin-top: 1rem;
        font-size: 1.2rem;
    }
</style>
""", unsafe_allow_html=True)

# Heading
st.markdown('<div class="main-title">🔢 Sum Calculator (1 to N)</div>', unsafe_allow_html=True)
st.markdown('<div class="desc-text">Enter a number and get the sum of numbers from 1 to N calculated using a loop.</div>', unsafe_allow_html=True)

# Input area (inline label)
st.markdown('<div class="input-container">', unsafe_allow_html=True)
st.markdown('<div class="input-label">📋 Enter a positive integer</div>', unsafe_allow_html=True)
n = st.number_input("Enter a number", min_value=1, step=1, format="%d", key="num_input", label_visibility="collapsed")
st.markdown('</div>', unsafe_allow_html=True)

# Calculate sum on button click
if st.button("✨ Calculate Sum"):
    total = 0
    breakdown = []
    for i in range(1, n + 1):
        total += i
        breakdown.append(str(i))

    st.markdown(
        f'<div class="result-box">✅ <strong>The sum of numbers from 1 to {n} is <span style="color:#004488;">{total}</span>.</strong></div>',
        unsafe_allow_html=True
    )

    with st.expander("🔍 Show Breakdown"):
        st.code(" + ".join(breakdown) + f" = {total}")
