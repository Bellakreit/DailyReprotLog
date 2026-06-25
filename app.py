import streamlit as st
# streamlit run app.py to run app
Home_page = st.Page("home.py", title="Home Page")  # creat home page
# create page for creating reports
create_report_page = st.Page("create_report.py", title="Create Report Page")  
all_reports_page = st.Page("all_reports.py", title="All Reports")  #  create report page
project_page = st.Page("project_page.py", title="Projects")  # create project page
worker_page = st.Page("worker_page.py", title="Workers")  # create worker page
feedback_page = st.Page("feedback.py", title="Feedback")  # create feedback page

pg = st.navigation([Home_page, create_report_page, all_reports_page, project_page, worker_page, feedback_page])  # make a navigation for the pages
st.set_page_config(page_title="Daily Report Log")  # keep browser consistent
pg.run()