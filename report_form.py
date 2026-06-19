import streamlit as st
import sqlite3
import pandas as pd

# @st.dialog("Report Form")
# def show_report_form():
#     with st.form("Report form"):
#         st.write("Fill in the missing details below.")
#         date = st.text_input("Date (YYYY-MM-DD): ")
#         safety = st.text_input("Safety: ")
#         description = st.text_input("Description of the days work: ")
#         worker_hours = st.text_input("Worker and Hours: ")
#         submitted = st.form_submit_button("Submit")
#         if submitted:
#             st.success("Report submitted successfully!")
#             st.rerun()

@st.dialog("Report Form")
def show_report_form():
    tab1, tab2, tab3 = st.tabs(["General", "Safety", "Worker Details"])

    with tab1:
        date = st.date_input("Date (YYYY-MM-DD):", key="date")
        description = st.text_area("Description of the day's work:", key="description", height=100)


    with tab2:
        st.write("Safety Equipment Used:")
        hard_hat_used = st.checkbox("Hard Hat Used", key="hard_hat_used")
        gloves_used = st.checkbox("Gloves Used", key="gloves_used")
        eye_protection_used = st.checkbox("Eye Protection Used", key="eye_protection_used")
        ear_protection_used = st.checkbox("Ear Protection Used", key="ear_protection_used")
        footware_used = st.checkbox("Footwear Used", key="footware_used")
        dust_mask_used = st.checkbox("Dust Mask Used", key="dust_mask_used")
        other_ppe_used = st.text_input("Other PPE Used:", key="other_ppe_used")

    with tab3:
        st.write("Worker Hours:")
        df = pd.DataFrame(columns=["Worker Name", "Hours Worked"])
        edit_df = st.data_editor(df, num_rows="dynamic", key="worker_hours_df")

    if st.button("Submit"):
        # access values via st.session_state.date, st.session_state.title, etc.
        conn = sqlite3.connect('report_log.db')  # replace with actual database connection
        submit_report(
            conn=conn,  # replace with actual database connection
            date=st.session_state.date,
            description=st.session_state.description,
            hard_hat_used=st.session_state.hard_hat_used,
            gloves_used=st.session_state.gloves_used,
            eye_protection_used=st.session_state.eye_protection_used,
            ear_protection_used=st.session_state.ear_protection_used,
            footware_used=st.session_state.footware_used,
            dust_mask_used=st.session_state.dust_mask_used,
            other_ppe_used=st.session_state.other_ppe_used
        )
        conn.close()
        st.success("Report submitted successfully!")
        st.session_state.show_form = False
        st.rerun()

def submit_report(conn, date, description, hard_hat_used, gloves_used, eye_protection_used, ear_protection_used, footware_used, dust_mask_used, other_ppe_used):
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO Reports (Date, Description, HardHatUsed, GlovesUsed, EyeProtectionUsed, EarProtectionUsed, FootwareUsed, DustMaskUsed, OtherPPEUsed)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', (date, description, hard_hat_used, gloves_used, eye_protection_used, ear_protection_used, footware_used, dust_mask_used, other_ppe_used))
    conn.commit()
