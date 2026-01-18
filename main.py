import speech_recognition as sr
import webbrowser
import musicLibrary
from gtts import gTTS
import pygame
from dotenv import load_dotenv
import os
from google import genai
import requests

load_dotenv(".env.local")

def speak(text):
    tts = gTTS(text)
    tts.save('temp.mp3') 

    # Initialize Pygame mixer
    pygame.mixer.init()

    # Load the MP3 file
    pygame.mixer.music.load('temp.mp3')

    # Play the MP3 file
    pygame.mixer.music.play()

    # Keep the program running until the music stops playing
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)
    
    pygame.mixer.music.unload()
    os.remove("temp.mp3") 

def aiProcess(command):

    client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

    response = client.models.generate_content(
        model="gemini-3-flash-preview",
        contents=[
            {
                "role": "system",
                "parts": [
                    {
                        "text": "You are a virtual assistant named Jarvis skilled in general tasks like Alexa and Google Assistant. Give short responses please."
                    }
                ]
            },
            {
                "role": "user",
                "parts": [
                    {
                        "text": command
                    }
                ]
            }
        ]
    )

    return response.text

def processCommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open facebook" in c.lower():
        webbrowser.open("https://facebook.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
    elif "open linkedin" in c.lower():
        webbrowser.open("https://linkedin.com")
    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        link = musicLibrary.music[song]
        webbrowser.open(link)

    elif "news" in c.lower():
        try:
            r = requests.get(f"https://newsapi.org/v2/everything?q=india&pageSize=5&sortBy=publishedAt&apiKey={os.getenv('NEWS_API_KEY')}", timeout=5)

            if r.status_code != 200:
                speak("Sorry, I could not fetch the news right now.")
                return

            data = r.json()
            articles = data.get("articles", [])

            if not articles:
                speak("No news available right now.")
                return

            speak("Here are the top headlines.")
            for article in articles[:5]:   
                speak(article["title"])

        except Exception as e:
            speak("There was an error while fetching the news.")
            print("News error:", e)


    else:
         # Let Gemini handle the request
        output = aiProcess(c)
        speak(output)


if __name__ == "__main__":                                                           
    speak("Intializing Jarvis....")
    while True:
       
        r = sr.Recognizer()

        # obtain audio from the microphone
        try:
            with sr.Microphone() as source:
                print("Listening...")
                audio = r.listen(source, timeout=4, phrase_time_limit=3)
            # recognize speech using Google
            print("recognizing...")
            word = r.recognize_google(audio)
            # Listen for the wake word "Jarvis
            if "jarvis" in word.lower():
                speak("Yes?")
                # Listen for command
                with sr.Microphone() as source:  
                    print("Jarvis Active...")
                    audio = r.listen(source, timeout=5, phrase_time_limit=4)
                    command = r.recognize_google(audio)
                    print("Command heard:", command)
    
                    processCommand(command)

        
        except Exception as e:
            print("Error; {0}".format(e))