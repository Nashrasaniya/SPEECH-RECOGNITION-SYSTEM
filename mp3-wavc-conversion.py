from pydub import AudioSegment

def convert_mp3_to_wav(mp3_file_path, wav_file_path):
    audio = AudioSegment.from_mp3(mp3_file_path)
    audio.export(wav_file_path, format="wav")

# Example usage:
mp3_path = r"C:\Users\MUBEEN\OneDrive\Documents\output.mp3"
wav_path = r"C:\Users\MUBEEN\OneDrive\Documents\output.wav"
convert_mp3_to_wav(mp3_path, wav_path)
