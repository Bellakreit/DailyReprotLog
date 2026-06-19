import streamlit as st
import pandas as pd
import sqlite3
from audiorecorder import audiorecorder
from report_form import show_report_form

st.title("Create Report", text_alignment="center")
st.header("Create a new report")
st.subheader("upload or record an audio to create your report")
st.logo("Designer.png", size='large')

# select project from dropdown from querying the database, no default value
conn = sqlite3.connect("report_log.db")
projects_df = pd.read_sql_query("SELECT * FROM Projects", conn)
project_names = projects_df["Name"].tolist()
selected_project = st.selectbox("Select Project", project_names, key="selected_project", placeholder=None)

uploaded_file = st.file_uploader(
    "Upload an audio file",
    type=["audio/mpeg", "audio/mp4", "audio/wav", "audio/x-wav"],
    help="Audio files are supported in mpeg, mp4, wav, and x-wav formats.",
)


st.title("Audio Recorder")
audio = audiorecorder("Click to record", "Click to stop recording")

if len(audio) > 0:
    # To play audio in frontend:
    st.audio(audio.export().read())  

    # To save audio to a file, use pydub export method:
    audio.export("audio.wav", format="wav")

btn_submit_audio = st.button("Submit Audio")
if btn_submit_audio:
    st.success("Audio submitted successfully!", show_report_form())

btnshow = st.button("Enter Report Manually")
if btnshow:
    show_report_form()
