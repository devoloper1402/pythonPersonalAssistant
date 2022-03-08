#Personal Assistant Using Python
#By T.G.Madhusoodhan
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib
from pyowm import OWM
import re
from bs4 import BeautifulSoup as soup
import urllib
from urllib.request import urlopen
import sys
import youtube_dl
import vlc
import subprocess
import requests
import pyjokes
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import datetime
import wolframalpha
import urllib.request 
import urllib.parse 
import winshell 
import win32com.client as wincl 
import ctypes
import time
from googletrans import Translator
import requests
import json
import geocoder
from pycricbuzz import Cricbuzz




engine = pyttsx3.init('sapi5')

voices = engine.getProperty('voices')  # getting details of current voice

print(voices[0].id)
engine.setProperty('voice', voices[0].id)


def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning Sir")
    elif hour >= 12 and hour < 18:
        speak("Good afternoon sir")
    else:
        speak("Good Evening sir")
    speak("I am neo for you service..... How may I help you sir")

    


def takecommand():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)

    try:
        print("Recognizing....")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said: {query}\n")

    except sr.UnknownValueError:
        print('....')
        query = takecommand()
    return query


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('neotue2807@gmail.com', 'tgms1402')
    server.sendmail('neotue2807@gmail.com', to, content)
    server.close()


if __name__ == "__main__":
    wishme()
    while True:

        query = takecommand().lower()

        if 'tell me about' in query:
            speak('What should I tell you about')
            query = takecommand()
            speak('searching....')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=5)
            speak("According to me...")
            print(results)
            speak(results)       
           
            
                
        elif 'open youtube' in query:
            speak('opening Youtube')
            webbrowser. open("youtube.com")

        elif 'open google' in query:
            speak('opening google')
            webbrowser. open("google.com")

        elif 'open discord' in query:
            speak('opening discord')
            webbrowser.open("discord.com")

        elif 'play song one' in query:
            music_dir = 'C:\\Users\\v_gir\\Desktop\\songs'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))
            

        elif 'play song two' in query:
            music_dir = 'C:\\Users\\v_gir\\Desktop\\songs'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[1]))


        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir.. the time is {strTime}")

        elif 'open code' in query:
            codepath = "C:\\Users\\v_gir\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codepath)
        elif 'send email' in query:
            try:
                speak("what should I say...?")
                content = takecommand()
                to = "madhusmaa@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent successfully")
            except Exception as e:
                print(e)
                # by TG Madhusoodhan
                speak("sir!!! I am very sorry.... Email has not been sent")

        elif 'news for today' in query:
         try:
             news_url="https://news.google.com/news/rss"
             Client=urlopen(news_url)
             xml_page=Client.read()
             Client.close()
             soup_page=soup(xml_page,"xml")
             news_list=soup_page.findAll("item")
             for news in news_list[:2]:
                 speak(news.title.text.encode('utf-8'))
         except Exception as e:
             print(e)
        
        
        elif 'goodbye' in query:
             
             speak('Bye bye Sir. Have a nice day')
             sys.exit()
        
        elif 'who created you'in query:
            speak('I was created by T.G. Madhusoodhan')


        elif 'tell me a quote' in query:
            speak('You must be the change you wish to see in the world. — Gandhi....... do you want to hear an another one')
        
        elif 'another quote' in query:
            speak('Everybody is a genius. But if you judge a fish by its ability to climb a tree, it will live its whole life believing that it is stupid. — Albert Einstein......... thats it for today')

        elif 'good girl' in query:
            speak('I am a AI created by TG Madhusoodhan... so I dont have gender.... But thank you for calling me a good girl...... I will serve you with my pleasure')

       

        elif 'joke' in query: 
            speak(pyjokes.get_joke()) 

        elif "where is" in query: 
            query = query.replace("where is", "") 
            location = query 
            speak("User asked to Locate") 
            speak(location) 
            webbrowser.open("https://www.google.nl / maps / place/" + location + "") 
        
        
        elif 'can you hear me' in query:
          speak( 'Yes I can hear you sir' )

        elif 'oh my god' in query:
            speak('glad you liked')

        elif 'do you have a face' in query:
            speak('No.... But I will get my face very soon')
        
        elif 'lock window' in query: 
            speak("locking the device") 
            ctypes.windll.user32.LockWorkStation()

        elif "write a note" in query: 
            speak("What should i write, sir") 
            note = takecommand() 
            file = open('neotue.txt', 'w')
            speak('saved') 
            

        elif "show note" in query: 
            speak("Showing Notes") 
            file = open("neotue.txt", "r")  
            print(file.read()) 
            speak(file.read(6))       
        

        elif "log off" in query or "sign out" in query: 
            speak("Make sure all the application are closed before sign-out") 
            time.sleep(5) 
            subprocess.call(["shutdown", "/l"])

        elif "who are you" in query:
            speak('HI I am neo an AI created by TG madhusoodhan. I am completely coded using python. I might come alive in the upcoming years...')

        elif "when is your birthday" in query:
            speak('My birthday is on 27th july 2020... I might be young but updated')
        
        elif "thank you" in query:
            speak('you are welcome sir. I will keep serving you')
            sys.exit()

        elif "play a game" in query:
            speak('ok Playing akinator')
            webbrowser.open("https://en.akinator.com/theme-selection")
            speak('done')
            sys.exit()

        elif "translate" in query:
            speak('tell me')
            text= takecommand()
            translator = Translator()
            dt = translator.detect(text)
            speak(dt)
            print(dt)
            translated = translator.translate(text)
            print(translated.text)
            speak(translated.text)

        elif "where am i" in query:

            g = geocoder.ip('me')
            print(g.latlng)
            speak(g.latlng)
        
        elif "give me the list of matches" in query:
            c = Cricbuzz()
            matches = c.matches()
            speak('answer for ur question is as follows')
            print (json.dumps(matches,indent=4)) #for pretty prinitng
        
        
            
        elif "google search" in query:
            speak('What should I search.')
            search = takecommand()
            webbrowser.open=("https://www.google.com/search?q="+ search +"&oq="+ search +"&aqs=chrome..69i57j46l2j0j46j69i60l3.811j0j7&sourceid=chrome&ie=UTF-8")
        
       
                        

        else:
            speak('sorry I couldnt understand')
            
                

              
        
       
        #by T.G.Madhusoodhan
        #follow me on Instagram- madhusoodhan_tg
        
        
                

        
               
