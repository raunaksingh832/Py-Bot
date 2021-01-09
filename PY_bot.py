'''Lets start!! '''
#This is a bot made by raunak singh like a dekstop assistant !
#To contact me :
#mail raunak.priya.dinkar@gmail.com
#Github raunak832 
#a student who studies in class 8 :)
import speech_recognition as sr
import pyttsx3 as speaker
import pywhatkit
import datetime
import smtplib
import getpass
import webbrowser
from tkinter import *
'''imported all required libraries'''
root = Tk()
root.title('Talking bot by-Raunak Singh')
root.geometry('1000x1000')
'''made a window using Tk() func of tkinter'''
def start():
    '''a func which has all the logic of the program'''
    listener = sr.Recognizer()
    engine = speaker.init()
    now = datetime.datetime.now()
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
                engine.say('lalalallalallaaalllaaaalalal lalalalal laaaaaaa laaa laa      was that good?   if not try saying play youtube music')
                engine.runAndWait()
            elif command == 'play youtube music':
                engine.say('give me the title of the video')
                engine.runAndWait()
                with sr.Microphone() as source0:
                    print('speak the title...')
                    voice1 = listener.listen(source0)
                    command1 = listener.recognize_google(voice1)
                    command = command.lower()
                    engine.say('playing music on yt it will take a little time')
                    engine.runAndWait()
                    pywhatkit.playonyt(command1)
            elif command == 'can you dance':
                engine.say('No! i cant i am a robot and robot cant dance    lol')
                engine.runAndWait()
            elif command == 'what is the time':
                engine.say('date is')
                engine.say('current date and tim,e is ')
                engine.say(now.strftime('%d-%m-%y'))
                engine.say('time is ')
                engine.say(now.strftime('%H-%M-%S'))
                engine.runAndWait()
            elif command == 'you are a good boy':
                engine.say('thanks for your appreciation i will be the loyalest to you ')
                engine.runAndWait()
            elif command == 'you are a bad boy':
                engine.say('i do not like you i am leaving you ')
                engine.runAndWait()
            elif command == 'get me some food':
                engine.say('i cant do that but you can do it by odering it on zomato or swiggy')
                engine.runAndWait()
            elif command == 'shut up':
                engine.say('U SHUT UP U CANT TALK TO A BOT LIKE THAT')
                engine.runAndWait()
            elif command == 'are you mad':
                engine.say('No i am not mad but i guess you are because you are asking stupid things')
                engine.runAndWait()

            elif 'song' in command:
                engine.say('The command is not right try using command play youtube music')
                engine.runAndWait()
            elif command == 'do nothing':
                engine.say('ok i will just sit on the couch and chill')
                engine.runAndWait()
            elif command == 'search on google':
                engine.say('what you want to search')
                engine.runAndWait()
                with sr.Microphone() as source4:
                    print('speak what you want to search ')
                    voice2 = listener.listen(source4)
                    command2 = listener.recognize_google(voice2)
                    command = command.lower()
                    engine.say('searching on google')
                    engine.runAndWait()
                    webbrowser.open(f'https://google.com/?#q={command2}')
            elif command == 'do a email':
                with sr.Microphone() as source:
                    engine.say('please speak what type of mail you want to send ')
                    engine.runAndWait()
                    print('speak...')
                    voice = listener.listen(source)
                    command = listener.recognize_google(voice)
                    for word in list(command):
                        if 'speak' in word:
                            with sr.Microphone() as source:
                                engine.say('please speak the subject of the email  ')
                                engine.runAndWait()
                                print('speak the subject.....')
                                voice = listener.listen(source)
                                sub = listener.recognize_google(voice)
                            with sr.Microphone() as source1:
                                print('speak the body of th mail....')
                                voice1 = listener.listen(source1)
                                body = listener.recognize_google(voice1)
                        elif 'type' in command:
                            engine.say('u have selected the type format')
                            engine.runAndWait()
                            sub = input('ENTER THE SUBJECT')
                            body = input('ENTER THE BODY')
                    smtp_object = smtplib.SMTP('smtp.gmail.com', 587)
                    smtp_object.ehlo()
                    smtp_object.starttls()
                    engine.say('please fill the formalities to send the mail')
                    engine.runAndWait()
                    email = input('email:')
                    password = getpass.getpass('password:')
                    smtp_object.login(email, password)
                    from_ = email
                    to = input('to whom you want to send:')
                    subject = sub
                    content = body
                    msg = 'Subject:' + subject + '\n' + content + '\n'
                    smtp_object.sendmail(from_, to, msg)
                    engine.say('email sent')
                    engine.runAndWait()
            else:
                engine.say('I dont know what you are speaking sorry')
                engine.runAndWait()

    except:
        engine.say('Your microphone is not working or there is a issue with your internet please try again later')
        engine.runAndWait()


lbl2 = Label(root, text='I am a bot made by Raunak Singh :)')
img = PhotoImage(file='Ai.png')
img2 = PhotoImage(file='Mic.gif')
lbl = Label(root, image=img, padx=200, pady=200)
button = Button(root, image=img2, command=start, padx=50, pady=50, fg='blue', bg='black')
button.place(x=0, y=0)
#making the backround of the window like buttons labels imgs etc.

lbl2.pack()
lbl.pack()
root.mainloop()
#start a loop which is looping through the screen to make the root work
#Finally Done!
