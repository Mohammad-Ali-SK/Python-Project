# a-z
# 0-9
# . _ time 1
# @ time 1
#  . seconor or third
# 

# from  instabot import Bot
# bot = Bot()
# bot.login(user='anonymous', passwd='',)
# # bot.follow("self/name")
# bot.upload("photo path")
# bot.unfollow("self/name")
# bot.send_massage("i love python", ['1','2','3'])
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    h = int(datetime.datetime.now().hour)
    if h >= 0 and h < 12:
        speak('Good Morning Sir')
    elif h >= 12 and h < 18:
        speak('Good After noon Sir.')
    else:
        speak("Good evening sir")
    speak('Please tell me sir how can i help  you.')

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening...')
        audio = r.listen(source)
    try:
        print('Recognizing....')
        query = r.recognize_google(audio,language = "en-in")
        print(f'User said : {query}')
    except Exception as e:
        print('Please say again.')
        return "None"
    return query
        
    
    
    
    
    

if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()
        
        if 'wikipedia' in query:
            speak('searching wikipedia.')
            query = query.replace('wikipedia',"")
            result = wikipedia.summary(query,sentences = 2)
            print(result)
            speak(result)
            