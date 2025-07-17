import streamlit as st

# Set page configuration
st.set_page_config(page_title="🎓 Student Score Evaluator", layout="centered")

# App Title
st.markdown("<h1 style='text-align: center; color: #4CAF50;'>📊 Student Score Evaluator</h1>", unsafe_allow_html=True)
st.write("### Enter your subject marks (between 1 and 100). All fields are required.")

# Subjects list
subjects = ["English", "Science", "Maths", "Hindi", "Tamil"]
scores = {}
errors = []
all_entered = True

# Input Fields in 2 Columns
cols = st.columns(2)

for i, subject in enumerate(subjects):
    with cols[i % 2]:
        value = st.text_input(f"{subject}:", placeholder="Enter marks", key=subject)

        if not value:
            all_entered = False
            continue

        try:
            score = int(value)
            if 1 <= score <= 100:
                scores[subject] = score
            else:
                errors.append(f"{subject} score must be between 1 and 100.")
                all_entered = False
        except ValueError:
            errors.append(f"{subject} must be a valid number.")
            all_entered = False

# Display errors if any
if errors:
    for err in errors:
        st.error(err)

# Show results
elif all_entered and len(scores) == len(subjects):
    total = sum(scores.values())
    average = total / len(subjects)
    min_score = min(scores.values())

    # Determine pass/fail
    passed = min_score >= 40 and average >= 50

    # Grade logic
    if average >= 90:
        grade = "A+"
    elif average >= 80:
        grade = "A"
    elif average >= 70:
        grade = "B"
    elif average >= 60:
        grade = "C"
    elif average >= 50:
        grade = "D"
    else:
        grade = "F"

    # Stylish Result Box
    st.markdown("---")
    st.markdown("### 📈 Your Performance Summary")
    with st.container():
        st.success(f"✅ **Total Marks:** {total} / 500")
        st.info(f"📊 **Average Score:** {average:.2f}%")
        st.info(f"🏅 **Grade:** {grade}")

    if passed:
        st.balloons()
        st.success("🎉 Congratulations! You have **Passed**.")
    else:
        st.error("❌ You have **Failed**. Please try again.")

else:
    st.info("ℹ️ Please fill in all subject marks to evaluate the result.")
