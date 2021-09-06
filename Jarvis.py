#this modue is used to access webbrowser                                                                             
import webbrowser

#this module is used to convert text into speech
import pyttsx3                       
import datetime

#this module is used to take recognise voice
import speech_recognition as sr      

#this module is used to access wikipedia
import wikipedia                     

#this is an AI module which is used to counter your question
import wolframalpha                  
import os 

#with this module you can access whatsapp
import pywhatkit as kit              

#this module is used to play mp3 sounds
from playsound import playsound      

#sapi5 is the voice recognition which is provided by Microsoft
engine = pyttsx3.init()
voices=engine.getProperty('voices')

#here index 0,1 is used to change voice of male and female
engine.setProperty('voice', voices[0].id)

#here wolframalpha module needs a client id to work
client=wolframalpha.Client('YR8J68-R2HWL9VA89')

# This Function will be used to speak

def speak(text):
    engine.say(text)
    engine.runAndWait()

# To wish the user

def wishme():
    hour=int(datetime.datetime.now().hour)
    if hour<=0 and hour>12:
        speak("Good morning sir")

    elif hour>=12 and hour<18:
        speak("good afternoon sir")

    else:
        speak("good evening sir")       
       
#This function will take command through microphone

def takecommand():                   
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold=2
        audio=r.listen(source)
    try:
        print("Recogizing...")
        query=r.recognize_google(audio)
        print(f"user Said {query}\n")

    except Exception as e:
        return "None"

    return query
 
if __name__=="__main__":
    wishme()

#Here jarvis is used as a trigger.
#whenever user speak jarvis the program starts taking the command

    wake= "jarvis"
    print("start")
    
    while True:
        query=takecommand().lower()
            
        if query.count(wake)>0:
            speak("yes sir!")
            query=takecommand().lower()

            if "goodbye" in query:
                speak('Goodbye Sir, Jarvis powering off in 3, 2, 1, 0')
                break

            elif "hello" in query or "Hi" in query:
                speak('Hello sir, how are you!')

            elif "thanks" in query  or "thank you" in query:
                speak("You are welcome")
                
            elif  "how are you" in query or "and you" in query or "are you okay" in query:
                speak("Fine thank you")

            elif "*" in query:
                speak("Please be polite")
 
            elif "your name" in query:
                speak("My name is Jarvis, at your service sir")                

            
            
            ############***************Webbrowser queries**************################ 

            elif "youtube" in query:
                speak("what i have to search sir")
                webbrowser.open("https://www.youtube.com/results?search_query=" + takecommand())

            elif "play" in query:
                src=takecommand()
                kit.playonyt(src)   

            elif "google" in query.lower():
                speak("what i have to search sir")
                webbrowser.open("https://www.google.co.in/?#q=" + takecommand())

            elif "stackoverflow" in query:
                speak("opening stackoverflow")
                webbrowser.open("https://stackoverflow.com/")

            elif "i have to attend a school class" in query:
                speak("Enter your meeting id sir")
                Gmeet_ID=input("Enter meeting ID:")
                webbrowser.open("https://meet.google.com/" +Gmeet_ID)
                speak("opening google meet")

            elif "open whatsapp"in query:
                speak("opening whatsapp")
                webbrowser.open("https://web.whatsapp.com/")

            elif "leetcode" in query:
                speak("opening leet code")
                webbrowser.open("https://www.leetcode.com/")

            elif "open gmail" in query:
                speak("opening gmail")
                webbrowser.open_new("https://gmail.com/")

            elif "memes"in query:
                speak("playing your memes sir")
                webbrowser.open("https://www.youtube.com/results?search_query=dank+indian+memes")

            elif "open instagram" in query:
                speak("opening instagram")
                webbrowser.open("https://www.instagram.com/?hl=en")    
            
           
           
            ############**************OS queries***************###########
        
            elif "shutdown the pc"in query:
                speak("are you sure sir!")
                query=takecommand().lower()
                if "yes" in query:
                    speak("shutting down the system")
                    os.system("shutdown/s /t 5")
                else:
                    speak("as your wish sir")        

            elif "open calculator"in query:
                speak("opening calculator")
                os.startfile("calc.exe")

            elif "open notepad"in query:
                speak("opening notepad")
                os.startfile("notepad.exe") 

            elif "open downloads"in query:
                speak("opening downloads")
                os.startfile("C://Users//HOME//Downloads")          

            else:
                query=query
                speak("searching...")
                try:
                    try:
                        res=client.query(query)
                        results=next(res.results).text
                        speak('wolframalpha says')
                        print(results)
                        speak(results)
                    
                    except:
                        results=wikipedia.summary(query, sentences=2)
                        speak('wikipedia says')
                        print(results)
                        speak(results)
                
                except:
                    webbrowser.open('https://www.google.co.in/')