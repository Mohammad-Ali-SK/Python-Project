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
import smtplib as s

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak('Good Mornig sir.')
    elif hour >= 12 and hour < 18:
        speak('Good Afternoon sir.')
    else:
        speak('Good evening sir.')
    speak('Hello MOhammad please tell me how can i help you.')
    
    
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening....')
        # r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print('Recognizing...')
        query = r.recognize_google(audio,language = "en-in")
        print(query)
    except Exception as e:
        print('Please say again...')
        return "None"
    return query

def sendEmail(sender,to):
    ob = s.SMTP('smpt.gmail.com',587)
    ob.ehlo()
    ob.starttls()
    ob.login({sender},"agpc vnjr nytn oqph")
    subject = takeCommand()
    print(subject)
    content = takeCommand()
    print(content)
    massage = "Subject: {}\n\n".format(subject,content)
    ob.sendmail({sender},{to},massage)
    ob.quit()    





if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()
        
        if 'wikipedia' in query:
            speak('Searching Wikipedia.')
            query = query.replace('wikipedia',"")
            result = wikipedia.summary(query,sentences =2)
            print(result)
            speak(result)
        
        elif 'open youtube'in query:
            webbrowser.open('youtube.com')
        
        elif 'open google' in query:
            webbrowser.open('Google.com')
        elif 'send email' in query:
            sendEmail("mohammdalisk01@gmail.com","mohammadalisk050@gmail.com")
        elif 'stop keen' in query:
            break