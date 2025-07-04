import streamlit as st
import requests

st.title("EduTutor AI - Quiz Generator")

# Backend API URL
backend_url = "http://127.0.0.1:8000/generate_quiz"

# Inputs
topic = st.text_input("Enter Topic", "additions")
difficulty = st.selectbox("Select Difficulty", ["Easy", "Medium", "Hard"])

if st.button("Generate Quiz"):
    # Send request to backend
    response = requests.post(backend_url, json={"topic": topic, "difficulty": difficulty})
    if response.status_code == 200:
        quiz = response.json()
        st.session_state['quiz'] = quiz
        st.session_state['answers'] = {}
        st.session_state['submitted'] = False

# Show quiz if generated
if 'quiz' in st.session_state:
    st.subheader(f"Quiz on {topic} ({difficulty})")

    for i, question in enumerate(st.session_state['quiz']['questions']):
        st.write(f"Q{i+1}: {question['question']}")
        selected = st.radio(f"Select your answer for Q{i+1}", question['options'], key=i)
        st.session_state['answers'][i] = selected

    if not st.session_state.get('submitted') and st.button("Submit Answers"):
        st.session_state['submitted'] = True
        score = 0
        for i, question in enumerate(st.session_state['quiz']['questions']):
            if st.session_state['answers'][i] == question['answer']:
                score += 1
        st.success(f"Your Score: {score} / {len(st.session_state['quiz']['questions'])}")