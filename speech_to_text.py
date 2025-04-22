import speech_recognition as sr
import os

# Function to transcribe audio
def transcribe_audio(file_path):
    recognizer = sr.Recognizer()

    # Check if file exists
    if not os.path.exists(file_path):
        print(" Audio file does not exist. Please check the path.")
        return

    # If file is not a .wav file, it needs to be converted before transcription.
    if not file_path.lower().endswith(".wav"):
        print(" The file is not a WAV file. Please provide a .wav file for transcription.")
        return

    try:
        with sr.AudioFile(file_path) as source:
            print(" Listening to the audio...")
            audio_data = recognizer.record(source)
            print(" Transcribing...")

            # Recognize speech using Google Web API
            text = recognizer.recognize_google(audio_data)
            print("\n Transcription:\n", text)

    except sr.UnknownValueError:
        print(" Could not understand the audio.")
    except sr.RequestError as e:
        print(f" Error with the recognition service: {e}")

# Replace this with your audio file path
file_path = r"C:\Users\MUBEEN\OneDrive\Documents\output.wav"  # Ensure the file is in .wav format
transcribe_audio(file_path)
