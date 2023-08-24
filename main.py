import speech_recognition as sr
import datetime
import subprocess
import pywhatkit
import pyttsx3
import webbrowser
import pyaudio

engine= pyttsx3.init()
voices= engine.getProperty('voices')
engine.setProperty('voices',voices[1].id)
recognizer= sr.Recognizer()

def cmd():
    with sr.Microphone() as source:
        print('Clearing background noise...Please wait...')
        recognizer.adjust_for_ambient_noise(source,duration=0.5)
        print('Hey Sakib..I am your personal voice assistant..Ask me anything..')
        recordedaudio= recognizer.listen(source)

    try:
        text = recognizer.recognize_google(recordedaudio, language='en_US')
        text = text.lower()
        print('Your message:', format(text))

    except Exception as ex:
        print(ex)

    if 'open chrome' in text:
        a = 'hey sakib i am john your personal voice assistant, i am opening chrome for you'
        engine.say(a)
        engine.runAndWait()
        webbrowser.open('www.google.com/chrome/')
    if 'time' in text:
        time = datetime.datetime.now().strftime('%I:%M %p')
        print(time)
        engine.say(time)
        engine.runAndWait()

    if 'play' in text:
        engine.say(a)
        engine.runAndWait()
        pywhatkit.playonyt(text)

    if 'hey john open youtube' in text:
        b = 'hey sakib i am john your personal voice assistant, i am opening youtube for you'
        engine.say(b)
        engine.runAndWait()
        webbrowser.open('www.youtube.com')
    if 'open youtube songs' in text:
        c = 'hey sakib i am john your personal voice assistant, i am opening songs from youtube for you'
        engine.say(c)
        engine.runAndWait()
        webbrowser.open('www.youtube.com/results?search_query=Trending+songs')

    if 'open east west university website' in text:
        d = 'hey sakib i am john your personal voice assistant, i am opening east west university website for you'
        engine.say(d)
        engine.runAndWait()
        webbrowser.open('www.ewubd.edu/')

    if 'open mohammad arif sir' in text:
        e = 'hey sakib i am john your personal voice assistant, i am opening east west university website for mohammad arifuzzaman '
        engine.say(e)
        engine.runAndWait()
        webbrowser.open('fse.ewubd.edu/electronics-communications-engineering/faculty-view/mazaman')

    if 'open facebook' in text:
        f = 'hey sakib i am john your personal voice assistant, i am opening facebook for you'
        engine.say(f)
        engine.runAndWait()
        webbrowser.open('www.facebook.com')

    if 'open email' in text:
        g = 'hey sakib i am john your personal voice assistant, i am opening email for you'
        engine.say(g)
        engine.runAndWait()
        webbrowser.open('www.gmail.com')
    if 'open map' in text:
        h = 'hey sakib i am john your personal voice assistant, i am opening map for you'
        engine.say(h)
        engine.runAndWait()
        webbrowser.open('www.google.com/maps')

    if 'open whatsapp' in text:
        i = 'hey sakib i am john your personal voice assistant, i am opening whatsapp for you'
        engine.say(i)
        engine.runAndWait()
        webbrowser.open('www.whatsapp.com')

    if 'open my portfolio' in text:
        i = 'hey sakib i am john your personal voice assistant, i am opening your portfolio on linked-in'
        engine.say(i)
        engine.runAndWait()
        webbrowser.open('bd.linkedin.com/in/sakib-morshed-28219a210?original_referer=https%3A%2F%2Fwww.google.com%2F')

    if 'east west university location in map' in text:
        j = 'hey sakib i am john your personal voice assistant, i am opening east west university location in map for you'
        engine.say(j)
        engine.runAndWait()
        webbrowser.open('www.google.com/maps/place/East+West+University/@23.7683804,90.4252649,19.43z/data=!4m6!3m5!1s0x3755c7892dcf0001:0x853ad729be4edc71!8m2!3d23.7685404!4d90.4255046!16zL20vMDkzMWRr')
    if 'open my portfolio' in text:
        i = 'hey sakib i am john your personal voice assistant, i am opening your portfolio on linked-in'
        engine.say(i)
        engine.runAndWait()
        webbrowser.open('https://bd.linkedin.com/in/sakib-morshed-28219a210')

while True:
    cmd()
    break






