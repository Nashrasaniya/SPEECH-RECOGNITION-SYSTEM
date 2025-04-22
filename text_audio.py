from gtts import gTTS
import os

def text_to_audio():
    # Prompt the user for input text
    text = input("Enter the text you want to convert to speech: ")

    # Prompt the user for the desired file path
    file_path = r"C:\Users\MUBEEN\OneDrive\Documents\output.mp3"


    # Ensure the directory exists
    os.makedirs(os.path.dirname(file_path), exist_ok=True)

    # Create a gTTS object
    tts = gTTS(text=text, lang='en', slow=False)

    # Save the audio to the specified file path
    tts.save(file_path)
    print(f"Audio saved as {file_path}")

# Call the function to execute
text_to_audio()
