import streamlit as st

# Set page config
st.set_page_config(page_title="Name Formatter", layout="centered")
st.title("📝 Name Formatter")

# Initialize session state
if "submitted" not in st.session_state:
    st.session_state.submitted = False
if "name_input" not in st.session_state:
    st.session_state.name_input = ""

# Handle reset (outside form, so it's triggered before input renders)
col1, col2 = st.columns([6, 1])
with col2:
    if st.button("🔄 Reset"):
        st.session_state.name_input = ""
        st.session_state.submitted = False
        st.rerun()

# Form input and submit
with col1:
    with st.form("name_form"):
        name = st.text_input("Enter your full name:", key="name_input")
        submit = st.form_submit_button("✅ Submit")
        if submit:
            st.session_state.submitted = True

# Show results
if st.session_state.submitted and st.session_state.name_input.strip():
    parts = st.session_state.name_input.strip().split()

    if len(parts) < 2:
        st.warning("⚠️ Please enter at least a first and last name.")
    else:
        first = parts[0]
        last = parts[-1]
        middle = " ".join(parts[1:-1]) if len(parts) > 2 else ""
        initials = "".join([p[0].upper() for p in parts])

        st.markdown("### 🔠 Formatted Versions:")
        st.write("**Original:**", st.session_state.name_input)
        st.write("**First Last:**", f"{first} {last}")
        st.write("**Last, First:**", f"{last}, {first}")
        st.write("**Initials:**", initials)

        if middle:
            st.write("**First Middle Last:**", f"{first} {middle} {last}")
            st.write("**Last First Middle:**", f"{last} {first} {middle}")
        else:
            st.write("**Last First:**", f"{last} {first}")

        st.write("**Uppercase:**", st.session_state.name_input.upper())
        st.write("**Lowercase:**", st.session_state.name_input.lower())
        st.success("✅ Name formatted successfully!")
