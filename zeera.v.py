import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import pywhatkit
import pyjokes
import smtplib
import requests
from bs4 import BeautifulSoup

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour < 12:
        speak("Good Morning!")
    elif 12 <= hour < 18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    speak("my name is Zeera . Please tell me how may I help you")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    except Exception as e:
        print("Say that again please...")  
        return "None"
    return query

def getHeadlines():
    url = "https://indianexpress.com/section/india/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    headlines = []
    for headline in soup.find_all('h2', class_='title'):
        headlines.append(headline.text.strip())
    return headlines



def run_assistant():
    wishMe()
    while True:
        query = takeCommand().lower()
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("https://www.youtube.com/")

        elif 'open google' in query:
            webbrowser.open("https://www.google.com/")

        elif 'open chrome' in query:
            webbrowser.open("C:\Program Files\Google\Chrome\Application\chrome.exe")

        elif 'open spotify' in query:
            webbrowser.open("https://www.spotify.com/")

        elif 'open msbte website' in query:
            webbrowser.open("https://msbte.org.in/")

        elif 'open chat gpt' in query:
            ##codePath = "https://chat.openai.com/"
            ##os.startfile(codePath)
            webbrowser.open("https://chat.openai.com/")
       
        elif 'play music' in query:
            music_dir = 'D:\music'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[1]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")

        elif 'open code' in query:
            codePath = "C:\\Users\\Haris\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif 'play ' in query:
            #song = Command.replace('play', '')
            song = query
            speak(song)
            #speak("playing" + song)
            pywhatkit.playonyt(song)

        elif 'joke' in query:
            joke = pyjokes.get_joke()
            print(joke)
            speak(joke)
        
        elif 'news headline' in query:
            speak("Fetching latest headlines.")
            headlines = getHeadlines()
            speak("Here are the top headlines for today:")
            for headline in headlines:
                speak(headline)

       

        elif 'shutdown' or 'exit' in query:
            speak("Thanks for giving me your time")


            exit()

            
run_assistant()