import streamlit as st
import json
import random

# 1. SETUP THE PAGE
st.set_page_config(page_title="HK Mock Interview Bot", layout="centered")
st.title("🎓 HK Primary School Interview Bot")
st.caption("Mock Interview Practice v1.0 (No-Code Prototype)")

# 2. LOAD QUESTIONS FROM FILE
def load_questions():
    with open('questions.json', 'r', encoding='utf-8') as f:
        return json.load(f)

try:
    data = load_questions()
    school_options = list(data.keys())
except FileNotFoundError:
    st.error("Error: questions.json file not found!")
    school_options = []

# 3. SIDEBAR - SETTINGS
with st.sidebar:
    st.header("⚙️ Settings")
    selected_school = st.selectbox("Choose Target School:", school_options)
    st.info("Currently in 'Mock Mode'. No voice recording yet.")

# 4. MAIN INTERFACE
if 'current_question' not in st.session_state:
    st.session_state.current_question = "Click 'Start' to get your first question."

col1, col2 = st.columns(2)

with col1:
    if st.button("▶️ Next Question", type="primary", use_container_width=True):
        # Logic: Pick a random question from the selected school
        questions_list = data[selected_school]
        st.session_state.current_question = random.choice(questions_list)

with col2:
    if st.button("🔄 Reset", use_container_width=True):
        st.session_state.current_question = "Ready to start."

# 5. DISPLAY THE QUESTION
st.divider()
st.subheader("📢 Interviewer asks:")
st.markdown(f"### {st.session_state.current_question}")
st.divider()

# 6. MOCK FEEDBACK SECTION
user_notes = st.text_area("Notes / Draft Answer (Optional):", height=100)

if st.button("📝 Generate Report (Mock)"):
    if user_notes:
        st.success("✅ Answer Recorded!")
        st.write("### 📊 Principal's Report (Sample)")
        st.write("- **Confidence:** 8/10")
        st.write("- **Vocabulary:** Good use of adjectives.")
        st.write("- **Advice:** Try to speak a bit slower and clearer.")
    else:
        st.warning("Please type some notes first.")
