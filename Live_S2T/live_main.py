import speech_recognition as sr
import static_ffmpeg
static_ffmpeg.add_paths()

import whisper
import os
from datetime import datetime

# 1. Model Loading
print("AI Model is Loading... Please wait.")
# Using base model for a balance between speed and accuracy
model = whisper.load_model("base")

# 2. File Setup (To store the transcription history)
filename = "transcription_history.txt"

def save_to_file(text):
    timestamp = datetime.now().strftime("%H:%M:%S")
    with open(filename, "a", encoding="utf-8") as f:
        f.write(f"[{timestamp}] {text}\n")

def listen_and_transcribe():
    recognizer = sr.Recognizer()
    
    with sr.Microphone() as source:
        print(f"\n--- System Ready! ---")
        print(f"Notes will be saved in: {os.path.abspath(filename)}")
        
        # 3. Ambient Noise Adjustment
        print("Adjusting for background noise...")
        recognizer.adjust_for_ambient_noise(source, duration=1)
        
        while True:
            try:
                print("Listening...", end="\r")
                # 4. Capturing Audio
                
                audio = recognizer.listen(source, phrase_time_limit=5)
                
                # 5. Writing Temporary Audio File
                
                with open("temp.wav", "wb") as f:
                    f.write(audio.get_wav_data())
                
                # 6. AI Transcription
                
                result = model.transcribe("temp.wav", fp16=False)
                text = result['text'].strip()
                
                if text:
                    print(f"Captured: {text}")
                    save_to_file(text)
                
            except KeyboardInterrupt:
                print("\n\nStopping session and cleaning up. Goodbye!")
                # Deleting the temporary audio file before exiting
                if os.path.exists("temp.wav"):
                    os.remove("temp.wav")
                break
            except Exception as e:
                print(f"\nError encountered: {e}")
                break

if __name__ == "__main__":
    listen_and_transcribe()