import pyttsx3 as pts
import webbrowser as wb
import datetime
import cv2
import wikipedia  as wiki
import speech_recognition as sr
import smtplib
import os
assistant_name= "Naavya"#"vyishu"#"whyzal"
owner="Manikanta"
engine=pts.init()
voices = engine.getProperty('voices')
engine.setProperty('gender', 'female')

#print(voices)
engine.setProperty('voice', voices[1].id)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    
#speak(assistant_name)
def time():
    speak("current time is ")
    time=datetime.datetime.now().strftime("%H:%M:%S")
    speak(time)
#time()
def date():
    year=int(datetime.datetime.now().year)
    month=int(datetime.datetime.now().month)
    day=int(datetime.datetime.now().day)
    speak("current date is")
    speak(day)
    speak(month)
    speak(year)
#date()
def wish(hour):
    if hour>=6 and hour<12:
        return "GOOD Morning"
    elif hour>=12 and hour <18:
        return "GOOD Afternoon"
    elif hour>=18 and hour <24:
        return "GOOD Evening"
    else:
        return "Good Night"
def wishme(owner):
    speak("welcome back "+owner)
    temp="this is"+assistant_name
    
    hour=datetime.datetime.now().hour
    speak(wish(hour))
    speak(temp)
    wishes="how can i help you?"
    speak(wishes)
    #speak(assistant_name+" at your service sir! how can i help you?")
#wishme()
def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening")
        r.pause_threshold=1
        audio=r.listen(source)
    try:
        print("recognising")
        #query=r.recognize_sphinx(audio)
        query=r.recognize_google(audio)
        print(query)
    except Exception as e:
        print(e)
        speak("say that again")
        return takeCommand()
    return query
#takeCommand()
def wikisearch(query):
    speak("Searching....")
    query=query.replace("wikipedia","")
    result=wiki.summary(query,sentences=2)
    speak(result)
''' this is not working as google improved its security for login and
it is less secured and can open gates to attacks of hackers if we
enable this type of login in our gmail account
def sendmail(to,content):#not succeeded
    server=smtplib.SMTP("smtp.gmail.com",587)
    server.ehlo()
    server.starttls()
    server.login("n160131@rguktn.ac.in","Mani@1234")
    server.sendmail("N160131@rguktn.ac.in",to,content)
    server.close()'''
def takepicture():
    speak("takeing picture....")
    vc=cv2.VideoCapture(0)
    ret,frame=vc.read()
    vc.release()
    speak("picture captured sir ...")
    if True:
        cv2.imshow("photo taken",frame)
        speak("do you want to save it sir...")
        query=takeCommand().lower()
        if "yes" in query or "save" in query:
            speak("by what name shall i save it sir...")
            query=takeCommand()+".jpg"
            cv2.imwrite(query,frame)
            cv2.destroyAllWindows()
    else:
        return        
def playsongs():
    path="D:\mine\music\songs"
    song=os.listdir(path)
    os.startfile(os.path.join(path,song[0]))
def screenshot():
    import pyautogui as pg
    img=pg.screenshot()
    img.save("ss.jpg")
    speak("screenshot is saved")
    
def cpu():
    import psutil as ps
    usage=ps.cpu_percent()
    speak("the cpu is at "+str(usage))
    
def battery():
    import psutil as ps
    battery=ps.sensors_battery()
    speak("battery at ")
    speak(battery.percent)
        
    
def joke():
    import pyjoke as pj
    speak(pj.get_joke())
    
