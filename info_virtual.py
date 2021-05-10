import speech_recognition as sr #recognise speechpip
import playsound #to play the audio file
from gtts import gTTS #goggle text so speech
import random
from time import ctime # time detials
import webbrowser
import ssl #This module provides access to Transport Layer Security (often known as “Secure Sockets Layer”) encryption and peer authentication facilities for network sockets, both client-side  and server-side.  This module uses the OpenSSL library
import certifi #Certifi provides Mozilla’s carefully curated collection of Root Certificates for validating the trustworthiness of SSL certificates while verifying the identity of TLS hosts. It has been extracted from the Requests project.
import time
import os #to remove the creted audio the files
from  PIL import Image #The Image module provides a class with the same name which is used to represent a PIL image. The module also provides a number of factory functions, including functions to load images from files, and to create new images.
import subprocess #The subprocess module allows you to spawn new processes, connect to their input/output/error pipes, and obtain their return codes
import pyautogui
import pyttsx3
import bs4 as bs #Beautiful Soup is a library that makes it easy to scrape information from web pages. 
import urllib.request #The urllib.request module defines functions and classes which help in opening URLs (mostly HTTP) in a complex world — basic and digest authentication, redirections, cookies and more.
#import wikipedia
class person:
    name=''
    def setName(self,name):
        self.name = name

class asis:
    name=''
    def setName(self,name):
        self.name = name
        
def there_exists(terms):
    for term in terms:
        if term in voice_data:
            return True
        
def engine_speak(text):
    text = str(text)
    engine.say(text)
    engine.runAndWait()
    
r = sr.Recognizer() #initialize a recogniser
#listen for audio and convert to text
def record_audio(ask=""):
    with sr.Microphone() as source:
        if ask:
            engine_speak(ask)
        
        audio =r.listen(source, 5, 5)#listen to audio via source
        print("Lokking the Database")
        voice_data = ''
        try :
            voice_data= r.recognize_google(audio)#convert audio to text
                 
        except sr.UnknownValueError: #error: reconizer doesn't understand

                engine_speak('Sorry sir, did not get that')
        except sr.RequestError:
                engine_speak("Sorry sir, server down")#error : recognizer is not connected
        print(">>", voice_data.lower())#print waht user said
        return voice_data.lower()
            
#get string and make audio file to be played
def engine_speak(audio_string):
    audio_string=str(audio_string) 
    tts = gTTS(text=audio_string , lang='en')#text to speech(voice)
    r = random.randint(1,20000000)
    audio_file='audio' + str(r) + '.mp3'
    tts.save(audio_file)#save as mp3
    playsound.playsound(audio_file)#to play the sound
    print(asis_obj.name +":",audio_string)#print what app said
    os.remove(audio_file)#remove the audio file ##let us check at last by comenting it whether it says
    
def respond(voice_data):
    # 1) if got greeting
    if there_exists(['hey','hi','hola','hello','wassup',]):
        greetings=["Hi sir, What we gonna do today?" +person_obj.name, "Hi sir, what are we doing today?" +person_obj.name, "Hi sir, How can i help you?"+person_obj.name]
        greet=greetings[random.randint(0,len(greetings)-1)]
        engine_speak(greet)
        
    #2))name
    if there_exists(["whta is your name","what's your name","tell me your name"]):
        if person_obj.name:
            engine_speak("whats with my name")
        else:
            engine_speak("I dont know my sir,please assighn my name by saying command your name should be ,,,,and sir will be priviledged to know your name ")
            
    if there_exists(["your name should be"]):
        asis_name =voice_data.split("be")[-1].strip()
        engine_speak("Okay sir,Ill remember my name"+asis_name)
        asis_obj.setName(asis_name)#remember name in asis object
        
    if there_exists(["my my name is"]):
        person_name = voice_data.split("is")[-1].strip()
        engine_speak("Okay sir ill remember your name is" + person_name)
        person_name.setName(person_name)#remember name in person object
        
    #3)) greeting
    if there_exists(["how are you bro","hoe are you","how are you doing"]):
        engine_speak("I m very well sir, how are you? thanks for asking")
        
    #4))time
    if there_exists(["whats the time","tell me the time","what time is it"]):
        time = ctime().split(" ")[3].split(":")[0:2]
        if time[0]=="00":
            hours='12'
        else:
            hours = time[0]
        minutes = time[1]
        time = hours + "hours and" + minutes + "minutes"
        engine_speak(time)
        
    #5))search google
    if there_exists(["search for"]) and 'youtube' not in voice_data:
        search_term=voice_data.split("for")[-1]
        url = "https://google.com/search?q=" + search_term
        webbrowser.get().open(url)
        engine_speak("Her is what i found for"+search_term + "on google")
        
    #6))) search youtube
    if there_exists(["search for youtube for","youtube"]):
        search_term=voice_data.split("for")[-1]
        url="https://www.youtube.com/results?search_query="+ search_term
        webbrowser.get().open(url)
        engine_speak("Here is what i found for "+ search_term + "on youtube")
        
    #7)) time table
    if there_exists(["show me my time table"]):
        im = Image.open(r"")
        im.show()
        
    #8))) get to know the weather
    if there_exists(["weather","how the weather outside","Please get the report of waether"]):
        search_term=voice_data.split("for")[-1]
        url="https://www.google.com/search?sxsrf=ACYBGNSQwMLDByBwdVFIUCbQqya-ET7AAA%3A1578847393212&ei=oUwbXtbXDN-C4-EP-5u82AE&q=weather&oq=weather&gs_l=psy-ab.3..35i39i285i70i256j0i67l4j0i131i67j0i131j0i67l2j0.1630.4591..5475...1.2..2.322.1659.9j5j0j1......0....1..gws-wiz.....10..0i71j35i39j35i362i39._5eSPD47bv8&ved=0ahUKEwiWrJvwwP7mAhVfwTgGHfsNDxsQ4dUDCAs&uact=5"
        webbrowser.get().open(url)#opens the webrowser
        engine_speak("Here is your report sir")
    
    #9)) get to know stock price
    if there_exists(["price of"]):
        search_term=voice_data.split("for")[-1]
        url="https://google.com/search?q="+ search_term
        webbrowser.get().open(url)
        engine_speak("Here is what i found for"+ search_term)
    
    # )#10 get to listen music
    # if there_exists("play music"):
    #     search_term=voice_data.split("for")[-1]
    #     url="https://open.spotify.com/search/"+search_term
    #     webbrowser.get().open(url)
    #     engine_speak("Enjoy sir"
    #11 screenshot
    if there_exists(["capture","my screen","screenshot"]):
        myScreenshot=pyautogui.screenshot()
        myScreenshot.save('')
        
    #4)) search wikipedia for defination
    
    if there_exists(["defination of"]):
        definition=record_audio("what do you need denination of")
        url=urllib.request.urlopen('https://en.wikipedia.org/wiki/'+definition)
        soup=bs.BeautifulSoup(url,'lxml')
        definitions=[]
        for paragraph in soup.find_all('p'):
            definitions.append(str(paragraph.txt))
        if definitions:
            if definitions[0]:#if condi is false
                engine_speak('i am sorry sir i could not find the definitios please try websearch')
            elif definitions[1]:#if condition is true
                engine_speak('here is what is found for'+ definitions[1])
            # else:
            # engine_speak('Here is what i found '+ definitions[2])
        else:
            engine_speak('i could not find the definition of'+definitions +'server down:user warning: have a websearch')

    #10 stone paper scisorrs
    if there_exists(["game"]):
        voice_data = record_audio("choose among rock paper or scissor")
        moves=["rock", "paper", "scissor"]
    
        cmove=random.choice(moves)
        pmove=voice_data
        

        engine_speak("The computer chose " + cmove)
        engine_speak("You chose " + pmove)
        #engine_speak("hi")


        if pmove==cmove:
            engine_speak("the match is draw")
        elif pmove== "rock" and cmove== "scissor":
            engine_speak("Player wins")
        elif pmove== "rock" and cmove== "paper":
            engine_speak("Computer wins")
        elif pmove== "paper" and cmove== "rock":
            engine_speak("Player wins")
        elif pmove== "paper" and cmove== "scissor":
            engine_speak("Computer wins")
        elif pmove== "scissor" and cmove== "paper":
            engine_speak("Player wins")
        elif pmove== "scissor" and cmove== "rock":
            engine_speak("Computer wins")

    #11 toss a coin
    if there_exists(["toss","flip","coin"]):
        moves=["head", "tails"]   
        cmove=random.choice(moves)
        engine_speak("The computer chose " + cmove)

    #12 calc
    if there_exists(["plus","minus","multiply","divide","power","+","-","*","/"]):
        opr = voice_data.split()[1]

        if opr == '+':
            engine_speak(int(voice_data.split()[0]) + int(voice_data.split()[2]))
        elif opr == '-':
            engine_speak(int(voice_data.split()[0]) - int(voice_data.split()[2]))
        elif opr == 'multiply':
            engine_speak(int(voice_data.split()[0]) * int(voice_data.split()[2]))
        elif opr == 'divide':
            engine_speak(int(voice_data.split()[0]) / int(voice_data.split()[2]))
        elif opr == 'power':
            engine_speak(int(voice_data.split()[0]) ** int(voice_data.split()[2]))
        else:
            engine_speak("Wrong Operator")
    # for exit       
    if there_exists(["exit","goodbye","quit","take some rest bro"]):
        engine_speak("We could continue more sir, well goodbye")
        exit()
        
        
time.sleep(1)

person_obj = person()
asis_obj = asis()
asis_obj.name = 'Nick'
engine = pyttsx3.init()
            
while(1):
    voice_data = record_audio("Recording") # get the voice input
    print("Done")
    print("Q:", voice_data)
    respond(voice_data) # respond
