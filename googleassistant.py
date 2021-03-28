import pyttsx3
import speech_recognition as sr
import datetime
import os
import cv2
import random
from requests import get
import wikipedia
import webbrowser
import pywhatkit as kit
import sys

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[0].id)   #check whose voice is in this machice change id 0 or 1
engine.setProperty('voices',voices[0].id)   #select voice of david which one on index 0

#text ot speech
def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()

#to convert voice into text
def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening.....")
        r.pause_threshold = 1
        audio = r.listen(source,timeout=1,phrase_time_limit=5)
    
    try:
        print("Recognizeing.....")
        query = r.recognize_google(audio,language='en-in')
        print(f"user said:{query}")

    except Exception as e:
        speak("Say that again Please....")
        return "none"
    return query

def wish():
    hour = int(datetime.datetime.now().hour)

    if hour>=0 and hour<=12:
        speak("good morning")
    elif hour>12 and hour<18:
        speak("good afternoon")
    else:
        speak("good evening")
    speak("i am jarvis Yunus sir, please tell me how can i help you ")


if __name__ == "__main__":
    wish()
    takecommand()

    while True:
        
        query = takecommand().lower()
        #logic buildin
        if "open notepad" in query:
            npath = "C:\\Windows\\system32\\notepad.exe"
            os.startfile(npath)

        elif "open command prompt" in query:
            os.system("start cmd")

        elif "open camera" in query:
            cap = cv2.VideoCapture(0)
            while True:
                ret , img = cap.read()
                cv2.imshow("webcam",img)
                k = cv2.waitKey(50)
                if k == 27:
                    break;
            cap.release()
            cv2.destroyAllWindows()

        elif "music" in query:
            music_dir = "D:\\musics"
            songs=os.listdir(music_dir)
            #rd=random.choice(songs) for random choice
            for song in songs:
                if song.endswith(".mp3"):
            #os.startfile(os.path.join(music_dir,rd)) for random songs play
                    os.startfile(os.path.join(music_dir,songs[0])) #for sequence play song

        elif "ip address" in query:
            ip = get("https://api.ipify.org").text
            speak(f"your ip address is {ip}")

        elif "wikipedia" in query:
            speak("searching wikipedia.....")
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query,sentences=2)
            speak("according to wikipeda")
            speak(results)
            print(results)

        elif "open youtube" in query:
            webbrowser.open("www.youtube.com")

        elif "facebook" in query:
            webbrowser.open("www.facebook.com")

        elif "stack overflow" in query:
            webbrowser.open("www.stackoverflow.com")

        elif "google" in query:
            speak("sir,what should i search on google.....")
            cm= takecommand().lower()
            webbrowser.open(f'{cm}')

        elif "find girl for me" in query:
            speak("sir you have already a girlfriend her name is ... Diksha")

       # elif "send message" in query:
       #     kit.sendwhatmsg("+919918209432","hii this is test",1.38)

        elif "play songs on youtube" in query:
            kit.playonyt("punjabi")

        elif "no thanks" in query:
            speak("thanks for using me sir have a good day ")
            sys.exit()

        speak("sir, do you have any other work")



    

