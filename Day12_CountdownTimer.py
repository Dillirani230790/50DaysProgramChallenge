import streamlit as st
import time

# Page config
st.set_page_config(page_title="🕒 Countdown Timer", layout="centered")

# CSS Styling
st.markdown("""
    <style>
    .header {
        text-align: center;
        font-size: 32px;
        font-weight: bold;
        color: #2c3e50;
        margin-top: 20px;
        margin-bottom: 30px;
    }
    .timer-box {
        font-family: 'Courier New', monospace;
        font-size: 32px;
        font-weight: bold;
        text-align: center;
        padding: 12px;
        margin: 30px auto 10px auto;
        width: 150px;
        border-radius: 10px;
        background-color: #d4edda; /* light green */
        color: #155724; /* dark green text */
        border: 2px solid #28a745;
        box-shadow: 0 0 6px rgba(0, 128, 0, 0.2);
    }
    .timer-box.red {
        background-color: white;
        color: red;
        border: 2px solid red;
    }
    .timeup-msg {
        text-align: center;
        font-size: 24px;
        color: red;
        font-weight: bold;
        margin-top: 10px;
    }
    .stButton>button {
        font-size: 18px;
        padding: 10px 30px;
        background-color: #007BFF;
        border: none;
        border-radius: 6px;
        color: white;
        transition: all 0.3s ease;
    }
    .stButton>button:hover {
        background-color: #0056b3;
        transform: scale(1.03);
    }
    audio {
        display: none;
    }
    </style>
""", unsafe_allow_html=True)

# Header
st.markdown("<div class='header'>⏳ Countdown Timer</div>", unsafe_allow_html=True)

# Input box
time_input = st.text_input("Enter countdown time in seconds:", value="", max_chars=3, placeholder="e.g., 10")

# Start button
start = st.button("Start Countdown")

# Beep audio (base64 encoded single beep sound)
beep_audio = """
<audio autoplay>
  <source src="data:audio/wav;base64,UklGRiQAAABXQVZFZm10IBAAAAABAAEAESsAACJWAAACABAAZGF0YQAAAAA=" type="audio/wav">
</audio>
"""

# Countdown logic
if start:
    if time_input.isdigit() and int(time_input) > 0:
        seconds = int(time_input)
        timer_placeholder = st.empty()
        message_placeholder = st.empty()

        for i in range(seconds, -1, -1):
            css_class = "timer-box" if i > 0 else "timer-box red"
            timer_html = f"<div class='{css_class}'>{i}</div>"
            timer_placeholder.markdown(timer_html, unsafe_allow_html=True)
            time.sleep(1)

        # Show "Time Up!" message
        message_placeholder.markdown("<div class='timeup-msg'>Time Up!</div>", unsafe_allow_html=True)

        # 3 beeps
        for _ in range(3):
            st.markdown(beep_audio, unsafe_allow_html=True)
            time.sleep(1)
    else:
        st.error("⛔ Please enter a valid positive number.")
