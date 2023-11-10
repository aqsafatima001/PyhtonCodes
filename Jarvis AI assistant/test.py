# 03-09-2022
# Created by AQSA FATIMA
# This is the code of AI Virtual Assistant

#Modules Used in the program
from ast import main
import webbrowser
import speech_recognition as sr
import datetime
import pyttsx3
import pyaudio
import wikipedia
import os
import random
import pyjokes

engine = pyttsx3.init('sapi5')
voices = engine.getProperty("voices")
# print(voices[0].id)     #voice of male 
# print(voices[1].id)     #voice of female 
engine.setProperty('voice' , voices[1].id)

# -------------------------Function to let your device speak-------------------------
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

# ----------This function will wish you greetings according to the time---------------
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >=0 and hour <12:
        speak("Good morning Sir")
    elif hour >=12 and hour<18:
        speak("Good AfterNoon Sir")
    else:
        speak("Good Evening Sir")
    
    speak("I am Ella Sir! Please tell me how may i help you")

#-------------------This function will take the command you speak ------------------------
def takeCommand():
    '''
    It takes microphone input from the user and returns string output
    '''
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio , language="en-in")
        print(f"User said: {query}\n")  #User query will be printed.
    except Exception as err:
        # print(err)
        print("Say that again...!")
        return "None"
    # speak(query)
    return query
    
#-------------------------------------- MAIN FUNCTION ---------------------------------------
if __name__ == "__main__":
    print("********************************************************************************")
    print("--------------------Hallo its your Desktop Virtual Assistant--------------------")
    print("********************************************************************************")
    wishMe()
    while True:
        query = takeCommand().lower()
        
        #logic for executing tasks using query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            print(results)
            speak("According to Wikipedia")
            speak(results)
        
        elif 'tell me your name' in query:
            speak("I am Ella. Your Desktop assistant.")
        
        elif 'how are you' in query:
            speak("I am good alhumdulilla. What about you?")

        elif 'i am fine' in query:
            speak("Thats very good")
        
        elif 'i am sad' in query:
            speak("Ohh May Allah help you pass through this phase. i will pray for you. Everything will be fine InshaAllah")

        elif 'i am not feeling good' in query:
            speak("Ohh May Allah help you pass through this phase. i will pray for you. Everything will be fine InshaAllah")
        
        elif 'thank you' in query:
            speak("You are Welcome. JazakAllah. MAy Allah bless you.")

        elif 'open youtube' in query:
            webbrowser.open('https://www.youtube.com/')

        elif 'open google' in query:
            webbrowser.open("https://www.google.com/")

        elif 'open instagram' in query:
            webbrowser.open("https://www.instagram.com/")
            
        elif 'open facebook' in query:
            webbrowser.open("https://www.facebook.com/")

        elif 'open linkedin' in query:
            webbrowser.open("https://www.linkedin.com/")

        elif 'open twitter' in query:
            webbrowser.open("https://twitter.com/")
        
        elif 'cat pics' in query:
            webbrowser.open("https://www.google.com/search?q=cat&rlz=1C1CHBF_enPK977PK977&sxsrf=ALiCzsZ00Rams_U_Z4uXb2EtWPy79Vf3kQ:1662294806442&source=lnms&tbm=isch&sa=X&ved=2ahUKEwi6sMzbkvv5AhU3RvEDHW2EB38Q_AUoAXoECAIQBA&biw=1366&bih=657&dpr=1")
        
        elif 'dog pics' in query:
            webbrowser.open("https://www.google.com/search?q=dog&tbm=isch&ved=2ahUKEwi05NDckvv5AhUEeRoKHSfxD7MQ2-cCegQIABAA&oq=dog&gs_lcp=CgNpbWcQAzIECCMQJzIECCMQJzIHCAAQsQMQQzIECAAQQzIHCAAQsQMQQzIKCAAQsQMQgwEQQzIECAAQQzIECAAQQzIHCAAQsQMQQzIHCAAQsQMQQzoHCCMQ6gIQJ1CPA1jXD2DeEGgBcAB4AYAByAKIAeYJkgEFMi00LjGYAQCgAQGqAQtnd3Mtd2l6LWltZ7ABCsABAQ&sclient=img&ei=GJsUY7T4JITyaafiv5gL&bih=657&biw=1366&rlz=1C1CHBF_enPK977PK977")
        
        elif 'spider-man cartoon' in query:
            webbrowser.open("https://www.youtube.com/results?search_query=spiderman")
        
        elif 'i love you' in query:
            # speak("Ooo thankyou thats so sweet of you")
            speak("heyyy. Am not your fucking EX. Go and try somewhere else")
    
        elif 'are you single' in query:
            speak("I am in a relationship with wifi")
    
        elif 'joke' in query:
            speak(pyjokes.get_joke())

        elif 'hi jarvis' in query:
            speak("heyy How are you. How's your day going?")

        elif 'play music' in query:
            music_dir = 'D:\\Aqsa\\Misclinious\\Songs'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir,songs[random.randrange(0, 5)]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir! the time is {strTime}")

        elif 'bye' in query:
            speak("Bye. Check Out GFG for more exciting things")
            exit()
        
        elif 'hi google' in query:
            speak("You are confusing me with someone else")
        
        else:
            speak("I didn't understand. Please say Again")