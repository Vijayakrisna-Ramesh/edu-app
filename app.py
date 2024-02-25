import streamlit as st

# Title of the application
st.title("Learning Goal LLM Agent")

# Input text box for learning goal with a character limit
goal = st.text_area("Enter your learning goal", max_chars=300)

# Dropdown for selecting duration
weeks = st.selectbox("Choose duration", [4, 8])

# Dropdown for selecting expertise level
expertise = st.selectbox("Select your expertise level", ["Beginner", "Expert"])

# Button to submit the user input
if st.button("Submit"):
    # For now, just display the input back to the user
    st.write(f"Learning Goal: {goal}")
    st.write(f"Duration: {weeks} weeks")
    st.write(f"Expertise Level: {expertise}")

    # Here, you would add the logic to call your LLM API and process the response
