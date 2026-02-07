import os
import random
import pygame
import speech_recognition as sr
import keyboard as kb
from puput import KeyboardSimulator

# Initialize pygame mixer for audio playback
pygame.mixer.init()

# Base directory where audio response folders are located
AUDIO_BASE_DIR = "audio_responses"
sim = KeyboardSimulator()

# Function to recognize speech from the microphone
def recognize_speech():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening for speech...")
        recognizer.adjust_for_ambient_noise(source)  # Adjust for ambient noise
        audio = recognizer.listen(source)  # Listen for speech input

        try:
            # Use Google Web Speech API for speech recognition
            text = recognizer.recognize_google(audio)
            print(f"You said: {text}")
            return text.lower()
        except sr.UnknownValueError:
            print("Could not understand the speech.")
            return None
        except sr.RequestError:
            print("Error with the speech recognition service.")
            return None
 
# Function to play a random audio file from the specified keyword directory
def play_custom_audio(keyword):
    keyword_dir = os.path.join(AUDIO_BASE_DIR, keyword)
    
    if os.path.exists(keyword_dir) and os.path.isdir(keyword_dir):
        audio_files = [f for f in os.listdir(keyword_dir) if f.endswith(('.wav', '.mp3', '.ogg'))]
        print(f"Files in '{keyword_dir}': {os.listdir(keyword_dir)}")

        if audio_files:
            random_file = random.choice(audio_files)
            file_path = os.path.join(keyword_dir, random_file)
            print(f"Playing {random_file} for keyword: {keyword}")
            
            pygame.mixer.music.load(file_path)
            pygame.mixer.music.play()
            while pygame.mixer.music.get_busy():
                pygame.time.Clock().tick(10)

        if keyword == "suspect killed":
            kb.press("F")
        
        if keyword == "civilian killed":
            kb.press("F")
            sim.simulate_key(0x21)
            sim.press_key(0x21)

        if keyword == "civilian in custody":
            kb.press("F")   

        else:
            print(f"No audio files found for keyword '{keyword}'.")
    else:
        print(f"No directory found for keyword '{keyword}'.")

# Continuous loop to listen and respond with custom audio
def main():
    while True:
        speech_text = recognize_speech()  # Recognize speech
        if speech_text:
            # Check if recognized speech matches any keyword and play custom audio
            play_custom_audio(speech_text)

            if "exit" in speech_text:  # Exit if "exit" is said
                print("Exiting program...")
                break  # Exit the loop

if __name__ == "__main__":
    main()
