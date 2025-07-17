import streamlit as st

# App title and description
st.set_page_config(page_title="Name Length Analyzer", layout="centered")
st.title("🧮 Name Length Analyzer")
st.write("Enter up to 5 names and see how long each one is!")

# Sidebar input
st.sidebar.header("✍️ Input Names")
names = []

for i in range(5):
    name = st.sidebar.text_input(f"Name {i+1}", key=f"name_{i}")
    name = name.strip()
    if name:
        names.append(name)

# Show total valid names entered
st.sidebar.markdown(f"**✅ Names Entered:** {len(names)}")

# Display results
st.subheader("📋 Results")

if names:
    for i, name in enumerate(names, 1):
        st.markdown(f"**{i}. {name}** — `{len(name)} characters`")
else:
    st.warning("Please enter at least one name in the sidebar.")

# Optional: Display summary
if len(names) == 5:
    longest_name = max(names, key=len)
    st.success(f"🏆 Longest Name: **{longest_name}** ({len(longest_name)} characters)")
