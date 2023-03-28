import time , pyttsx3 , speech_recognition as sr
from functions import *

# Variables 
i = ''
ra = pyttsx3.init()
ra.setProperty('rate',150)
r = sr.Recognizer()



with sr.Microphone() as source:
    r.adjust_for_ambient_noise(source)
    ra.say('look at our services and tell us What do you want me to do ?')
    ra.runAndWait()
    audio = r.listen(source)
try:
    text = r.recognize_google(audio)
    print("You demanded : " + text)
    i = text
except sr.UnknownValueError:
    print("Google Speech Recognition could not understand audio")
except sr.RequestError as e:
    print("Could not request results from Google Speech Recognition service; {0}".format(e))


def record(question) :
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        ra.say(question)
        ra.runAndWait()
        audio = r.listen(source)
        text = r.recognize_google(audio)
        return text
i = i.lower()
if i == 'search about something' :
    text = record('what do you wanna search about ?')
    try: 
        Orders.SearchAboutSomething(text)
    except :
        pass 
elif i == 'search in youtube' :
    text = record('what do you wanna search about ?')
    try: 
        Orders.SearchInYoutube(text)
    except :
        pass 
elif i == 'open an application' :
    text = record('which application do you want to open ?')
    try: 
        Orders.OpenAnApp(text)
    except :
        pass 
elif i == 'open a website' :
    text = record('which website do you want to visit ?')
    try: 
        Orders.OpenWebSite(text)
    except :
        pass 
else :
    try :
        record('Sorry , we cannot do your order')
    except :
        pass