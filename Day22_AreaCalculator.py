import streamlit as st
import math

# ---------- PAGE CONFIG ----------
st.set_page_config(page_title="🧮 Area Calculator", layout="centered")

# ---------- TITLE ----------
st.markdown("<h1 style='color:#4CAF50;'>📐 Area Calculator</h1>", unsafe_allow_html=True)
st.markdown("<p style='color:gray;'>Select a shape, enter dimensions, and get the area instantly!</p>", unsafe_allow_html=True)
##st.markdown("---")

# ---------- UNIT SELECTION ----------
unit = st.selectbox("🌍 Select unit of measurement", ["meters", "feet", "inches"])
unit_symbol = {"meters": "m", "feet": "ft", "inches": "in"}[unit]

# ---------- SHAPE SELECTION ----------
shape = st.radio("📊 Choose a shape", ["Circle", "Rectangle", "Triangle"], horizontal=True)

# ---------- INPUT SECTION ----------
st.markdown("### ✏️ Enter dimensions")
inputs = {}

if shape == "Circle":
    inputs["radius"] = st.number_input(f"🌀 Radius ({unit_symbol})", min_value=0.0, step=0.1)
elif shape == "Rectangle":
    inputs["length"] = st.number_input(f"📏 Length ({unit_symbol})", min_value=0.0, step=0.1)
    inputs["width"] = st.number_input(f"📐 Width ({unit_symbol})", min_value=0.0, step=0.1)
elif shape == "Triangle":
    inputs["base"] = st.number_input(f"📐 Base ({unit_symbol})", min_value=0.0, step=0.1)
    inputs["height"] = st.number_input(f"📏 Height ({unit_symbol})", min_value=0.0, step=0.1)

# ---------- CALCULATION FUNCTION ----------
def calculate_area(shape, **kwargs):
    if shape == "Circle":
        return math.pi * kwargs["radius"] ** 2
    elif shape == "Rectangle":
        return kwargs["length"] * kwargs["width"]
    elif shape == "Triangle":
        return 0.5 * kwargs["base"] * kwargs["height"]

# ---------- BUTTONS ----------
col1, col2 = st.columns([1, 1])

with col1:
    if st.button("✅ Calculate Area"):
        if any(v <= 0 for v in inputs.values()):
            st.error("❗ Please enter valid positive values for all inputs.")
        else:
            area = calculate_area(shape, **inputs)
            st.success(f"🎉 Area of the {shape.lower()} is: **{area:.2f} {unit_symbol}²**")

with col2:
    if st.button("🔄 Clear"):
        st.experimental_rerun()

# ---------- FOOTER ----------
st.markdown("---")
st.markdown(
    "<p style='text-align: center; color: #999;'>❤️",
    unsafe_allow_html=True
)
