from logging import exception
import sys
import cv2
import pyttsx3
import speech_recognition as sr
import datetime
import os
import wikipedia
import webbrowser
import sys
import pyjokes



#variables
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices',voices[0].id)

#converts text to speech
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    print(audio)

def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source,timeout=1,phrase_time_limit=5)

    try:
        print("Recognising...")
        query = r.recognize_google(audio,language=("en-in"))
        print(query)

    except exception as e:
        speak("Sorry pls say that again")
        return 'none'
    return query

def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<=12:
        speak("Good Morning")
    elif hour>=12 and hour<=18:
        speak("Good Afternoon")
    else:
        speak("Good Evening")
    speak("I'm Jarvis, How may I help you?")
    


if __name__ == '__main__':
    wishme()
    while True:
        query = takecommand().lower()
        #all the tasks

        if 'open notepad'in query:
            npath = "C:\\WINDOWS\\system32\\notepad.exe"
            os.startfile(npath)
           
        elif 'open command prompt' in query:
            os.system("start cmd")

        elif 'open chrome' in query:
            cpath = "C:\Program Files\Google\Chrome\Application\chrome.exe"
            os.startfile(cpath)
            speak("Okay done")
        
        elif 'open camera' in query:
            cap = cv2.VideoCapture(0)
            while True:
                ret, image = cap.read()
                cv2.imshow('webcam', image)
                k = cv2.waitKey(50)
                if k==27:
                    break;
            cap.release()
            cv2.destroyAllWindows()

        elif 'play music' in query:
            musicdir = 'C:\\Users\\tohiba\\Music\\Favourites'
            songs = os.listdir(musicdir)
            os.startfile(os.path.join(musicdir, songs[4]))

        elif 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace('wikipedia',"")
            results = wikipedia.summary(query, sentences=2)
            speak('According to wikipedia...')
            speak(results)
            speak('What else can I do?')

        elif 'open youtube' in query:
            webbrowser.open('www.youtube.com')
            speak('Anything else you want me to do?')

        elif 'close youtube' in query:
            speak('Okay, Closing Youtube...')
            os.system('taskkill /f /im chrome.exe')

        elif 'open google' in query:
            speak('What should I search on google?')
            cm = takecommand().lower()
            webbrowser.open(f'{cm}')
            speak('What else can I do?')

        elif 'joke' in query:
            joke = pyjokes.get_joke()
            speak(joke)
            speak('Anything else you want me to do?')

        elif 'thanks'in query:
            speak('Thank you for using me, Have a great day')
            sys.exit()

        elif 'set an alarm':
            nn = int(datetime.datetime.now().hour)
            if nn == 11:
                music = 'C:\\Users\\tohiba\Music\\Favourites'
                songs = os.listdir(music)
                os.startfile(os.path.join(music, songs[0]))

        elif 'close the alarm' in query:
            speak('Okay Closing the alarm...')
            os.system('taskkill/ f /im Groove_Music.exe')

        else:
            speak('Sorry, that is out of my understanding')


