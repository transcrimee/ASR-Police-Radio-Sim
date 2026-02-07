import speech_recognition as sr
import pyttsx3
import pygame
import os

# Initialize pygame mixer for audio playback
pygame.mixer.init()

# Function to recognize speech from the microphone
def recognize_speech():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening for speech...")
        recognizer.adjust_for_ambient_noise(source)  # Optional: Adjust for ambient noise
        audio = recognizer.listen(source)  # Listen for speech input

        try:
            # Use Google Web Speech API for speech recognition
            text = recognizer.recognize_google(audio)
            print(f"You said: {text}")
            return text
        except sr.UnknownValueError:
            print("Could not understand the speech.")
            return None
        except sr.RequestError:
            print("Error with the speech recognition service.")
            return None

# Function to play custom audio file based on keyword
def play_custom_audio(keyword):
    # Dictionary of keywords and corresponding audio files
    audio_randomselector = {
        "hello": "\hello",  # Example custom audio for "hello"
        "goodbye": "goodbye_audio.wav",  # Example custom audio for "goodbye"
        "help": "help_audio.wav",  # Example custom audio for "help"
        "attention": "GP_ATTENTION_UNIT.wav",  # Custom audio for "attention"
       "show me unseen":"GP_TEN_FOUR_02.wav",
    }

    # Print the current working directory to help debug
    print(f"Current directory: {os.getcwd()}")

    # Check if keyword exists in the dictionary
    if keyword.lower() in audio_files:
        audio_file = audio_files[keyword.lower()]
        if os.path.exists(audio_file):  # Check if the audio file exists
            print(f"Playing custom audio for keyword: {keyword}")
            pygame.mixer.music.load(audio_file)  # Load the custom audio file
            pygame.mixer.music.play()  # Play the audio file
            while pygame.mixer.music.get_busy():  # Wait until audio finishes
                pygame.time.Clock().tick(10)
        else:
            print(f"Audio file for '{keyword}' not found.")
    else:
        print(f"No custom audio for '{keyword}'.")

# Continuous loop to listen and respond with custom audio
def main():
    while True:
        speech_text = recognize_speech()  # Recognize speech
        if speech_text:
            # Check if recognized speech contains any keyword and play custom audio
            play_custom_audio(speech_text)

            # Comment or remove this line to disable the narrator voice
            # text_to_audio(speech_text)  # This line produces the narrator voice

            if "exit" in speech_text.lower():  # Exit if "exit" is said
                print("Exiting program...")
                break  # Exit the loop

if __name__ == "__main__":
    main()
