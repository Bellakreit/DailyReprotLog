import streamlit as st
import sqlite3

st.title("Please give us your feedback")

if "show_form" not in st.session_state:  # default for the form is false until the button is clicked
    st.session_state.show_form = True

# show the form
st.session_state.show_form = True

if st.session_state.show_form:  # if the form should be shown
    with st.form("Feedback_form"):  # made the form
        st.write("Please provide your feedback below:")
        stars = st.slider("Rate our service (1-5 stars):", 1, 5, 3)
        comment = st.text_area("Comments:")
        change = st.text_area("What would you like to see changed or improved? (Optional):")
        fix = st.text_area("What specific issues have you encountered? (Optional):")
        # make submit button
        submit_button = st.form_submit_button("Submit Feedback")
        if submit_button:
            # Process the feedback
            conn = sqlite3.connect('report_log.db')
            cursor = conn.cursor()
            cursor.execute('''
                INSERT INTO Feedback (UserID, Stars, Comment, Change, Fix)
                VALUES (?, ?, ?, ?, ?)
            ''', (1, stars, comment, change, fix))
            conn.commit()
            conn.close()
            st.success("Feedback submitted successfully!")
            st.session_state.show_form = False