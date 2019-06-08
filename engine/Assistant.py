import pyttsx3
import random
import datetime
import webbrowser
import wikipedia
import os
from weather import Weather, Unit
import speech_recognition as sr
engine = pyttsx3.init()
#voices = engine.getProperty('voices')
#for voice in voices:
#    if voice.languages[0] == u'en_US':
#        engine.setProperty('voice', voice.id)
#        break
engine.setProperty('rate',150)
engine.setProperty('volume',10)
greetings = ['hey there','hello','hey']
questions = ['how are you doing', 'how is it going',"how are you"]
responses = ['okay','good', 'i am fine']
var1 = ["what is the time","what time is it now","time"]
var2 = ["who are you","what is your name"]
cmd1 = ["open browser","open google"]
cmd2 = ["play music"]
cmd3 = ["open leafpad"]
cmd4 = ["tell me about weather","how is the weather"]
cmd5 = ["close","exit","bye","nothing"]
rep = ["you are welcome","glad I could help you"]
cmd6 = ["open code","open vs code"]
cmd7 = ["anaconda","open anaconda"]
while True:
    now = datetime.datetime.now()
    r = sr.Recognizer()    
    with sr.Microphone() as source:        
        os.system("echo 'Please wait for 5 seconds. Calibrating microphone...'")        
        r.adjust_for_ambient_noise(source, duration=5) 
        os.system("echo 'Say something'")        
        audio = r.listen(source)
        try:
            print("You said:- " + r.recognize_google(audio))           
        except sr.UnknownValueError:
            print("Could not understand audio")            
            engine.say('I didnt get that. Rerun the code')
            engine.runAndWait()
    if r.recognize_google(audio) in greetings:
        random_greeting = random.choice(greetings)
        print(random_greeting)        
        engine.say(random_greeting)
        engine.runAndWait()
    elif r.recognize_google(audio) in questions:
        engine.say('I am fine')
        engine.runAndWait()
        print('I am fine')      
       
    elif r.recognize_google(audio) in cmd2:
       os.system("spotify")
    elif r.recognize_google(audio) in var2:
        engine.say('I am a voice assistant made for ubuntu')
        engine.runAndWait()
    elif r.recognize_google(audio) in cmd3:
        os.system('leafpad')
   
    elif r.recognize_google(audio) in cmd4:
        weather = Weather(unit=Unit.CELSIUS)
        lookup = weather.lookup(560743)
        condition = lookup.condition
        print(condition.text)
        
    elif r.recognize_google(audio) in var1:
        print("Current date and time : ")        
        print(now.strftime("The time is %H:%M"))        
        engine.say(now.strftime("The time is %H:%M"))
        engine.runAndWait()
    elif r.recognize_google(audio) in cmd1:
        webbrowser.open('www.google.com')
        
    elif r.recognize_google(audio) in cmd5:
        os.system("echo'see you later'")
        
        engine.say('see you later')
        engine.runAndWait()
        exit()
        
    elif r.recognize_google(audio) in cmd6:
        os.system("code")
        os.system("echo 'opening vs code'")
        
    elif r.recognize_google(audio) in cmd7:
        os.system("anaconda-navigator")
        os.system("echo 'opening anaconda'")
    else:
        engine.say("please wait")
        engine.runAndWait()
        print(wikipedia.summary(r.recognize_google(audio)))
        
        engine.say(wikipedia.summary(r.recognize_google(audio)))
        engine.runAndWait()
        userInput3 = input("or else search in google")
        webbrowser.open_new('www.google.com/search?q=' + userInput3)
