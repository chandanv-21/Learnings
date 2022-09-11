import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import random
import smtplib
import sys
# import pyaudio

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[0].id)
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good morning!")
    elif hour>=12 and hour<18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    speak("I Am Jarvis. Please tell me sir how may I help you....")

def takeCommand():
    '''It will take the input from user microphone and returns string output.
    '''
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening......")
        r.pause_threshold = 1
        r.energy_threshold = 400
        audio = r.listen(source)
    try:
        print("Recognizing......")
        query = r.recognize_google(audio, language='en-in') 
        print(f"User Said {query}\n")

    except Exception as e:
        # print(e)
        print("Say that again please.")
        return "None"
    return query

def sendEmail(to, content):
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('rairavi222@gmail.com','Ravi@123')
    server.send('rairavi222@gmail.com',to,content)
    server.close()

if __name__ == '__main__':

    wishMe()
    while True:
        query=takeCommand().lower()
        """Logic for executing task based on query"""
        if "wikipedia" in query:
            speak("Searching Wikipedia....")
            query= query.replace("wikipedia", "")
            result = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            print(result)
            speak(result)

        elif "youtube" in query:
            webbrowser.open("youtube.com")

        elif "open google" in query:
            webbrowser.open("google.com")

        elif "open stackoverflow" in query:
            webbrowser.open("stackkoverflow.com")

        elif "play music" in query:
            music_dir = 'E:\\Chandan\\Music'
            songs = os.listdir(music_dir)
            song_num=random.randint(0, len(songs)-1)
            print(len(songs))
            print(song_num)
            os.startfile(os.path.join(music_dir,songs[song_num]))

        elif "time" in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, The time is {strTime}")

        elif "open code" in query:
            path = "C:\\Users\\DELL\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(path)

        elif "send email to chandan" in query:
            try:
                speak("what should I say")
                content=takeCommand()
                to= "vishwakarmachandan910@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent to Chandan")
            except Exception as e:
                print(e)
                speak("Sorry bro Email could not be sent")

        elif "quit" in query:
            sys.exit()