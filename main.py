import speech_recognition as sr
import musicLibrary
import webbrowser
import pyttsx3
import requests

engine = pyttsx3.init()
newsapi = "949c588e496b4351b94ac65788d5c843https://newsapi.org/v2/top-headlines?country=in&apiKey=949c588e496b4351b94ac65788d5c843"

def speak(text):
    engine.say(text)
    engine.runAndWait()

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
        r = requests.get(f"https://newsapi.org/v2/top-headlines?country=in&apiKey={newsapi}")
        if r.status_code == 200:
            # Parse the JSON response
            data = r.json()
            
            # Extract the articles
            articles = data.get('articles', [])
            
            # Print the headlines
            for article in articles:
                speak(article['title'])

    


if __name__ == "__main__":                                                           
    speak("Intializing Jarvis....")
    while True:
        # Listen for the wake word "Jarvis"
        # obtain audio from the microphone
        r = sr.Recognizer()
        

        print("recognizing...")
        # recognize speech using Google
        try:
            with sr.Microphone() as source:
                print("Listening...")
                audio = r.listen(source, timeout = 2, phrase_time_limit=1)
            word = r.recognize_google(audio)
            if(word.lower() == "jarvis"):
                speak("Ya")
                # Listen for command
                with sr.Microphone() as source:
                    print("Jarvis Active...")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)

                    processCommand(command)

        
        except Exception as e:
            print("Error; {0}".format(e))