import pyttsx3  # pip install pyttsx3
import speech_recognition as sr  # pip insall speechRecogintion

import datetime
import wikipedia  # pip install wikipedia
import webbrowser
import os
import smtplib
import pyaudio
MASTER = "Master Belal"

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


# speak function will pronounce the string which is passed to it

def speak(text):
    engine.say(text)
    engine.runAndWait()


# This funtion will wish you as per current time
def wishMe():
    hour = int(datetime.datetime.now().hour)
    speak("its {} O clock".format(hour))
    if 0 <= hour < 12:
        speak("Good Morning " + MASTER)
    elif 12 <= hour < 18:
        speak("Good Afternoon " + MASTER)
    else:
        speak("Good Evening " + MASTER)


# this funtion wiill take comand from microphone
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listning ...")
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language= "en-in")
        print(f"user said: {query}\n")
    except Exception as e:
        print("Say that again please")
        query = None
        return query





# main program strts form here
speak("Initialising khaleesi....")
wishMe()
query =  takeCommand()

# logic for executing tasks as per the query

if 'wikipedia' in query.lower():
    speak('Searching in wikipeia')
    query = query.replace("wikipedia", "")
    results = wikipedia.summary(query, sentences=2)
    print(results)
    speak(results)
elif 'open youtube' in query.lower():
    webbrowser.open("youtube.com")
    
