import streamlit as st
import pandas as pd
import time
import os
import pyttsx3
from streamlit_extras.add_vertical_space import add_vertical_space

# Function to speak welcome message
def speak_welcome():
    engine = pyttsx3.init()
    engine.say("Welcome to Growth Mindset Project, made by Jareer Shafiq")
    engine.runAndWait()

# Ensure welcome message plays only once per session
if 'welcome_spoken' not in st.session_state:
    speak_welcome()
    st.session_state['welcome_spoken'] = True

# Set Page Config with Dark Mode
st.set_page_config(page_title='Growth Mindset Hub', layout='wide', initial_sidebar_state='expanded')

# Custom CSS for Enhanced Gradient and Vibrant UI
st.markdown(
    """
    <style>
        body {
            background: linear-gradient(135deg, #1a1a2e, #16213e);
            color: white;
            font-family: 'Arial', sans-serif;
        }
        .main-header {
            font-size: 2xl;
            font-weight: bold;
            text-align: center;
            background: -webkit-linear-gradient(left, #ff4b1f, #1fddff);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            margin-bottom: 20px;
        }
        .footer {
            text-align: center;
            font-size: 2xl;
            font-weight: bold;
            margin-top: 20px;
        }
        .chatbot-icon {
            position: fixed;
            bottom: 20px;
            right: 20px;
            background: #ff4b1f;
            color: white;
            padding: 10px 15px;
            border-radius: 50%;
            cursor: pointer;
            font-size: 20px;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# Header
st.markdown("<h1 class='main-header'>🚀 Growth Mindset Hub by Jareer Shafiq</h1>", unsafe_allow_html=True)

# Chatbot Section
st.sidebar.subheader("🤖 Growth Mindset Chatbot")
st.sidebar.write("Hello! I'm here to guide you through your journey of self-improvement. Let me know how I can help!")
chatbot_input = st.sidebar.text_area("Type your question here:")

chatbot_responses = {
    "What is Growth Mindset?": "A growth mindset is the belief that abilities and intelligence can be developed through dedication and hard work.",
    "How to stay motivated?": "Set small achievable goals, stay consistent, and remind yourself of your purpose!",
    "Tips for self-improvement?": "Read books, meditate, exercise, and maintain a journal to track progress.",
}

if st.sidebar.button("Submit"):
    response = chatbot_responses.get(chatbot_input, "I'm not sure about that, but keep learning and growing!")
    st.sidebar.write(f"🤖 {response}")

# User Input Section in the Center
st.subheader("📝 Daily Growth Tracker")
name = st.text_input("Enter Your Name", "Guest")
age = st.number_input("Enter Your Age", min_value=10, max_value=100, step=1)
profession = st.text_input("Enter Your Profession")

if st.button("Let's Begin 🚀"):
    st.session_state['started'] = True

if 'started' in st.session_state:
    st.subheader("How are you feeling today?")
    feelings = st.multiselect("Select your current feelings:", ["I feel Happy", "I feel Sad", "I feel Stressed", "I feel Tired"])
    
    if "I feel Happy" in feelings:
        st.success("Happiness is contagious! Keep spreading positivity! 😊")
    if "I feel Sad" in feelings:
        st.warning("Tough times don't last, but tough people do. Stay strong! 💪")
    if "I feel Stressed" in feelings:
        st.info("Breathe in, breathe out. You're capable of handling this! 🌿")
    if "I feel Tired" in feelings:
        st.error("Rest is important. Recharge and come back stronger! 🔋")
    
    st.subheader("⚡ Energy Level Tracker")
    energy_level = st.slider("Rate your energy level for today:", 0, 100, 50)
    st.write(f"Your energy level is: {energy_level}")
    
    st.subheader("🏆 Daily Challenges & Tasks")
    challenge = st.text_area("Set your daily challenge:")
    if st.button("Save Challenge"):
        st.session_state['challenge'] = challenge
    
    if 'challenge' in st.session_state:
        st.write("### Your Challenge:")
        st.write(st.session_state['challenge'])
    
    st.subheader("📖 Mindfulness Exercises")
    if st.button("Start Breathing Exercise"):
        st.write("Breathe in... Hold... Breathe out...")
    
    st.subheader("✅ Habit Tracker")
    habit_options = ["Read a book", "Meditate", "Drink Water", "Journal Writing"]
    selected_habits = {}
    
    for habit in habit_options:
        selected_habits[habit] = st.checkbox(habit)
    
    quotes = {
        "Read a book": "A reader lives a thousand lives before he dies. 📖",
        "Meditate": "Quiet the mind, and the soul will speak. 🧘‍♂️",
        "Drink Water": "Stay hydrated, stay healthy! 💧",
        "Journal Writing": "Fill your paper with the breathings of your heart. ✍️"
    }
    
    for habit, selected in selected_habits.items():
        if selected:
            st.write(f"**{habit}** - {quotes[habit]}")
    
    st.sidebar.subheader("User Profile")
    st.sidebar.write(f"**Name:** {name}")
    st.sidebar.write(f"**Age:** {age}")
    st.sidebar.write(f"**Profession:** {profession}")
    
    st.markdown("### Remember: Small steps lead to big changes. Keep pushing forward! 🌟")
