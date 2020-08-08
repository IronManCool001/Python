import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib
import pygame

pygame.init()

screen = pygame.display.set_mode((900, 720))

background = pygame.image.load('jarvis.png')

pygame.display.set_caption('J.A.R.V.I.S')




engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices)
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >=0  and hour <12:
        speak('Good Morning!')
    elif hour >=12 and hour<18:
        speak('Good Afternoon')
    else:
        speak('Good Evening')

    speak('I am Jarvis')
    #speak('I  am created by Debaditya Malakar') 
    speak('How may I help you')


def takeCommand():
    '''It takes microphone input from the user and returns string output'''

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening.....')
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print('Recognizing....')
        query = r.recognize_google(audio, Language='en-in')
        print(f"User said: {query} \n")

    except Exception as e:
        #print(e)
        print('Say that again please....')
        return "None"
    return query


if __name__ == "__main__":
    wishMe()

    while True:
        query = takeCommand().lower()
        screen.blit(background, [0,0])
        pygame.display.update()
    #Logic for execution task based on query
    if 'wikipedia' in query:
        speak('Searching Wikipedia')
        query = query.replace('Wikipedia','')
        results = wikipedia.summary(query, sentences=2)
        speak('According to wikipedia')
        speak(results)

    elif 'open youtube' in query:
        webbrowser.open("youtube.com")

    elif 'open google' in query:
        webbrowser.open('google.com')

    elif 'open stackoverflow' in query:
        webbrowser.open('stackoverflow.com')

    elif 'play music' in query:
        music_dir = 'C:\\Users\\Devaditya\\Music'
        songs = os.listdir(music_dir)
        print(songs)
        os.startfile(os.path.join(music_dir, songs[0]))

    elif 'the time' in query:
        strTime = datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"Sir, the time is{strTime}")

    elif 'open code' or 'open vscode' in query:
        codePath = "C:\\Program Files\\Microsoft VS Code\\Code.exe"
        os.startfile(codePath)

    elif 'send email' in query:
        try:
            server = smtplib.SMTP('smtp.gmail.com', 587)
            speak("What should I say?")
            content = takeCommand()
            speak("Which email should I sent to...")
            rec_email = takeCommand()
            server.ehlo()
            server.starttls()
            server.login('pankajsur60@gmail.com', 'linux-android')
            server.sendmail('pankajsur60@gmail.com', rec_email, content)
            server.close()
            speak('Email has been sent successfuly')
        except Exception as e:
            print(f"Problem:{e}")
            with open('log.txt','a') as f:
                f.write(f"The problem is {e}")
            speak('Sorry I am unable to send the email doe to some problem')

    elif 'exit' in query:
        exit()

