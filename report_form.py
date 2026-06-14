import streamlit as st

# @st.dialog("Report Form")
# def show_report_form():
#     with st.form("Report form"):
#         st.write("Fill in the missing details below.")
#         date = st.text_input("Date (YYYY-MM-DD): ")
#         title = st.text_input("Title: ")
#         safety = st.text_input("Safety: ")
#         description = st.text_input("Description of the days work: ")
#         worker_hours = st.text_input("Worker and Hours: ")
#         submitted = st.form_submit_button("Submit")
#         if submitted:
#             st.success("Report submitted successfully!")
#             st.rerun()

@st.dialog("Report Form")
def show_report_form():
    tab1, tab2, tab3 = st.tabs(["General", "Safety", "Work Details"])

    with tab1:
        date = st.date_input("Date (YYYY-MM-DD):", key="date")
        title = st.text_input("Title:", key="title")

    with tab2:
        safety = st.text_area("Safety:", key="safety",height=100)

    with tab3:
        description = st.text_area("Description of the day's work:", key="description", height=100)
        worker_hours = st.text_input("Worker and Hours:", key="worker_hours")

    if st.button("Submit"):
        # access values via st.session_state.date, st.session_state.title, etc.
        st.session_state.show_form = False
        st.rerun()