# import smtplib as s

# ob = s.SMTP('smtp.gmail.com',587)
# ob.ehlo()
# ob.starttls()
# ob.login("mohammadalisk01@gmail.com","agpc vnjr nytn oqph")
# subject = input('Enter the subject.')
# body = input('Enter the massage content..')
# massage = "subject: {}\n\n{}".format(subject,body)
# listadd = ['mohammadalisk050@gmail.com','mohammadalisk060@gmail.com']
# ob.sendmail("mohammadalisk01@gmail.com",listadd,massage)
# ob.quit()


import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser


engine = pyttsx3.init("sapi5")
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    h = int(datetime.datetime.now().hour)
    if h >= 0 and h < 12:
        speak("Good Mornig sir.")
    elif h >= 12 and h < 18:
        speak('Good Afternoon Sir.')
    else:
        speak("Good evening sir.")
    speak("Hello sir i am ali please tell me how can i help you.")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening...')
        audio = r.listen(source)
    try:
        print("Recognizing....")
        query = r.recognize_google(audio,language = "en-in")
        print(f"User Said : {query}")
    except Exception as e:
        print("Pleasse say again.")
        return "None"
    return query


if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()
        if "wikipedia" in query:
            print('Searching wikipeida.')
            query = query.replace('wikipedia',"")
            result = wikipedia.summary(query,sentences=2)
            print(result)
            speak(result)
        elif "open youtube" in query:
            webbrowser.open("youtube.com")
        elif "open google" in query:
            webbrowser.open("google.com")
        elif "the time" in query:
            time = datetime.datetime.now().strftime("%H:%M:%S")
            speak(time)
            
            