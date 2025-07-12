import streamlit as st

st.title("🧾 Total Cost Calculator (with Tax)")

# Function to safely convert input to float
def safe_float(value):
    try:
        return float(value)
    except:
        return 0.0

# Input as text to allow blank placeholder and on-focus entry
item1 = safe_float(st.text_input("Enter price of Item 1", placeholder="e.g. 100"))
item2 = safe_float(st.text_input("Enter price of Item 2", placeholder="e.g. 200"))
item3 = safe_float(st.text_input("Enter price of Item 3", placeholder="e.g. 300"))
tax_percentage = safe_float(st.text_input("Enter tax percentage (%)", placeholder="e.g. 18"))

# Calculate total when button is pressed
if st.button("Calculate Total"):
    subtotal = item1 + item2 + item3
    tax_amount = subtotal * (tax_percentage / 100)
    total_cost = subtotal + tax_amount

    st.write(f"**Subtotal:** ₹{subtotal:.2f}")
    st.write(f"**Tax Amount:** ₹{tax_amount:.2f}")
    st.success(f"**Total Cost (incl. tax): ₹{total_cost:.2f}**")
