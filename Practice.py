import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    h = int(datetime.datetime.now().hour)
    
    if h > 0 and h < 12:
        speak('Good Morning sir.')
    elif h > 12 and h < 18:
        speak('Good After noon sir')
    else:
        speak('Good evening sir')
    speak("Hello sir i am JARVIS how can i help you")
    
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening....')
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print('Recognizing....')
        query = r.recognize_google(audio,language='en-in')
        print(f"User Said : {query}")
    except Exception as e:
        print("please say again..")
        return "None"
    return query
    
    
    

if __name__ == "__main__":
    wishMe()
    
    while True:
        query = takeCommand().lower()
        if 'wikipedia' in query:
            speak('Searching wikipedia')
            query = query.replace('wikipedia','')
            result = wikipedia.summary(query,sentences=2)
            print(result)
            speak(result)
            