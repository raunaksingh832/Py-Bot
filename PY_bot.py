import pyaudio
import speech_recognition as sr
import pyttsx3 as speaker
import pywhatkit
import datetime
now = datetime.datetime.now()
listener = sr.Recognizer()
engine = speaker.init()
engine.say('What can I do for you')
engine.runAndWait()
try:
    with sr.Microphone() as source:
        print('listening....')
        voice = listener.listen(source)
        command = listener.recognize_google(voice)
        command = command.lower()
        if command == 'are you there':
            engine.say('yes! i am always there for you i am the loyalest')
            engine.runAndWait()
        if command == 'play music':
            engine.say('Taalllaaaalalal lalalalal laaaaaaa laaa laa      was that good?   if not try saying play youtube music')
            engine.runAndWait()
        if command == 'play youtube music':
            engine.say('give me the title of the video')
            engine.runAndWait()
            with sr.Microphone() as source1:
                print('speak the title...')
                voice1 = listener.listen(source1)
                command1 = listener.recognize_google(voice1)
                command = command.lower()
                engine.say('playing music on yt it will take a little time')
                engine.runAndWait()
                pywhatkit.playonyt(command1)
        if command == 'can you dance':
            engine.say('No! i cant i am a robot and robot cant dance    lol')
            engine.runAndWait()
        if command == 'what is the time':
            engine.say('current date and time is ')
            engine.say('date is')
            engine.say(now.strftime('%d-%m-%y'))
            engine.say('time is ')
            engine.say(now.strftime('%H-%M-%S'))
            engine.runAndWait()
        if command == 'you are a good boy':
            engine.say('thanks for your appreciation i will be the loyalest to you ')
            engine.runAndWait()
        if command == 'you are a bad boy':
            engine.say('i do not like you i am leaving you ')
            engine.runAndWait()
        if command == 'get me some food':
            engine.say('i cant do that but you can do it by odering it on zomato or swiggy')
            engine.runAndWait()
        if command == 'shut up':
            engine.say('U SHUT UP U CANT TALK TO A BOT LIKE THAT')
            engine.runAndWait()
        if command == 'are you mad':
            engine.say('No i am not mad but i guess you are because you are asking stupid things')
            engine.runAndWait()    
        else:
            engine.say('I dont know what you are speaking')
            engine.runAndWait()
        
except:
    engine.speak('Your microphone is not working')
    engine.runAndWait()

