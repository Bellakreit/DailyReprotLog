import streamlit as st
import pandas as pd
import sqlite3

st.title("Project Page", text_alignment="center")

conn = sqlite3.connect("report_log.db")
df = pd.read_sql_query("SELECT * FROM Projects", conn)
edit_df = st.data_editor(df, num_rows="dynamic", key="project_df")

if st.button("Save"):
    # save back to database
    edit_df.to_sql("Projects", conn, if_exists="replace", index=False)
    st.success("Project details saved successfully!")
    conn.close()
