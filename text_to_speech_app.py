import streamlit as st
from gtts import gTTS
import os

# Function to synthesize speech from text
def synthesize_speech(text):
    tts = gTTS(text=text, lang='en')
    audio_file = "output.mp3"
    tts.save(audio_file)
    return audio_file

# Title and input area in the Streamlit app
st.title("Text to Speech Converter")
text_input = st.text_area("Enter text to convert to speech:")

# Convert button
if st.button("Convert to Speech"):
    if text_input:
        audio_file = synthesize_speech(text_input)
        st.audio(audio_file)
        st.download_button(label="Download Audio", data=open(audio_file, 'rb'), file_name="output.mp3")
    else:
        st.warning("Please enter some text before converting!")
