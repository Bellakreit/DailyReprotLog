import streamlit as st
import pandas as pd
import sqlite3

st.title("Worker Page", text_alignment="center")

conn = sqlite3.connect("report_log.db")
df = pd.read_sql_query("SELECT * FROM Workers", conn)
edit_df = st.data_editor(df, num_rows="dynamic", key="worker_df")

if st.button("Save"):
    # save back to database
    edit_df.to_sql("Workers", conn, if_exists="replace", index=False)
    st.success("Worker details saved successfully!")
    conn.close()
