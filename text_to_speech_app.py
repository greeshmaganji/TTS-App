import streamlit as st  # Import Streamlit
from gtts import gTTS   # Import gTTS for text-to-speech
import os


# Function to synthesize speech from text, language, and speed
def synthesize_speech(text, language, slow):
    tts = gTTS(text=text, lang=language, slow=slow)
    audio_file = "output.mp3"
    tts.save(audio_file)
    return audio_file

# Title in the Streamlit app
st.title("Text to Speech Converter")

# Input area for text
text_input = st.text_area("Enter text to convert to speech:")

# Dropdown for selecting the language
language_options = {
    'English (US)': 'en',
    'English (UK)': 'en-uk',
    'French': 'fr',
    'Spanish': 'es',
    'German': 'de',
    'Hindi': 'hi',
    'Telugu': 'te',
    'Tamil': 'ta'
}
language = st.selectbox("Select language:", list(language_options.keys()))

# Option to choose slow or fast speech
speed = st.radio("Choose speech speed:", ('Normal', 'Slow'))

# Convert button
if st.button("Convert to Speech"):
    if text_input:
        # Get the selected language code and speed
        language_code = language_options[language]
        is_slow = True if speed == 'Slow' else False
        
        # Generate the audio file
        audio_file = synthesize_speech(text_input, language_code, is_slow)
        
        # Play the audio file and provide download option
        st.audio(audio_file)
        st.download_button(label="Download Audio", data=open(audio_file, 'rb'), file_name="output.mp3")
    else:
        st.warning("Please enter some text before converting!")
