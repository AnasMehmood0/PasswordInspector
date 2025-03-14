import streamlit as st
import re

# Set page configuration
st.set_page_config(page_title="Password Inspector", page_icon="🔐", layout="centered")

# Custom CSS for dark purple gradient theme, animations, and styling
st.markdown("""
    <style>
    /* Apply dark purple gradient to the entire app */
    .stApp {
        background: linear-gradient(135deg, #4A148C, #6A1B9A, #8E24AA);
        color: white;
        font-family: 'Arial', sans-serif;
        padding: 2rem;
        border-radius: 15px;
        border: 4px solid #AB47BC;
        box-shadow: 0px 0px 20px rgba(171, 71, 188, 0.5);
    }

    /* Ensure all text is visible */
    .stMarkdown, .stTextInput, .stButton, .stInfo, .stSuccess, .stWarning, .stError {
        color: white !important;
    }

    /* Style the input label */
    .stTextInput label {
        color: #E1BEE7 !important;
        font-size: 18px;
        font-weight: bold;
    }

    /* Glowing animation for the title */
    @keyframes glow {
        0% { text-shadow: 0 0 5px #E1BEE7; }
        50% { text-shadow: 0 0 20px #E1BEE7, 0 0 30px #AB47BC; }
        100% { text-shadow: 0 0 5px #E1BEE7; }
    }

    h1 {
        animation: glow 2s infinite;
        color: #E1BEE7;
        text-align: center;
        font-size: 3rem;
        margin-bottom: 1rem;
    }

    /* Animation for the input field */
    .stTextInput input {
        background: linear-gradient(135deg, #E1BEE7, #CE93D8);
        border: 2px solid #AB47BC;
        border-radius: 10px;
        color: #4A148C;
        padding: 10px;
        font-size: 16px;
        transition: all 0.3s ease;
    }

    .stTextInput input:focus {
        border-color: #E1BEE7;
        box-shadow: 0px 0px 10px rgba(225, 190, 231, 0.5);
    }

    /* Button styling */
    .stButton button {
        background-color: #AB47BC;
        color: white;
        border: none;
        border-radius: 10px;
        padding: 10px 20px;
        font-size: 16px;
        transition: all 0.3s ease;
        width: 100%;
    }

    .stButton button:hover {
        background-color: #E1BEE7;
        color: #4A148C;
        box-shadow: 0px 0px 10px rgba(225, 190, 231, 0.5);
    }

    /* Progress bar styling */
    .stProgress > div > div {
        background-color: #AB47BC !important;
        border-radius: 10px;
    }

    /* Feedback message styling */
    .feedback-message {
        padding: 10px;
        border-radius: 10px;
        margin: 10px 0;
        background-color: rgba(171, 71, 188, 0.2);
        border-left: 4px solid #AB47BC;
        animation: slideIn 0.5s ease-in-out;
    }

    @keyframes slideIn {
        from { opacity: 0; transform: translateX(-20px); }
        to { opacity: 1; transform: translateX(0); }
    }

    /* Color-coded feedback */
    .strong {
        color: #28B463 !important;
    }
    .medium {
        color: #D4AC0D !important;
    }
    .weak {
        color: #E74C3C !important;
    }
    </style>
    """, unsafe_allow_html=True)

# Title and description
st.title("Password Inspector 🔑🔒🔓🗝️🛡️")
st.markdown("""
            ## Safe. Secure. Passwords 
            #### Examine, Strengthen, Protect: Password Inspector analyzes your passwords and provides expert recommendations to safeguard your digital identity.
            """)

# Password input (visible, not hidden)
password = st.text_input("Enter your password", type="default", placeholder="Type your password here...")

# Initialize feedback list and score
feedback = []
score = 0

# Check password button
if st.button("Check Password 🔍"):
    if password:
        # Length check
        if len(password) >= 8:
            score += 1
        else:
            feedback.append("❌ Password is too short (minimum 8 characters required).")

        # Uppercase and lowercase check
        if re.search("[A-Z]", password) and re.search("[a-z]", password):
            score += 1
        else:
            feedback.append("❌ Password should contain both uppercase and lowercase letters.")

        # Digit check
        if re.search("[0-9]", password):
            score += 1
        else:
            feedback.append("❌ Password should contain at least one digit.")

        # Special character check
        if re.search("[_*@$#]", password):
            score += 1
        else:
            feedback.append("❌ Password should contain at least one special character (e.g., _, *, @, $, #).")

        # Strength feedback
        if score == 4:
            feedback.append("✅ Your password is strong! 🔒")
            st.balloons()  # Celebrate strong password
        elif score == 3:
            feedback.append("⚠️ Your password is medium. Consider improving it. 🔓")
        else:
            feedback.append("❌ Your password is weak. Please strengthen it. 🔓")

        # Display feedback
        if feedback:
            st.markdown("### Password Analysis & Improvement Suggestions:")
            for tip in feedback:
                if "strong" in tip:
                    st.markdown(f'<div class="feedback-message strong">{tip}</div>', unsafe_allow_html=True)
                elif "medium" in tip:
                    st.markdown(f'<div class="feedback-message medium">{tip}</div>', unsafe_allow_html=True)
                else:
                    st.markdown(f'<div class="feedback-message weak">{tip}</div>', unsafe_allow_html=True)

        # Progress bar for password strength
        st.progress(score / 4)
    else:
        st.warning("🔑 Please enter a password to check.")
