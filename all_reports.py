import streamlit as st

def btnSeeAllReports_Click():
    st.session_state.show_all_reports = True

see_all = st.button("See All Reports", type="primary", on_click=btnSeeAllReports_Click)
search_query = st.text_input("Search by title or date (YYYY-MM-DD)", help="Enter a title or date to search for specific reports.")

if "show_all_reports" not in st.session_state:
    st.session_state.show_all_reports = False  

if st.session_state.show_all_reports:
    st.subheader("All Reports")
    # Here you would typically fetch and display the reports from your database
    # For demonstration, we'll just show a placeholder message
    st.write("Displaying all reports... (This is where your report data would appear)")
    st.dataframe({
        "Title": ["Report 1", "Report 2", "Report 3"],
        "Date": ["2023-01-01", "2023-01-02", "2023-01-03"],
    })
