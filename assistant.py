from Basic_functions import *
if __name__=="__main__":
    wishme(owner)
    while 1:
        query=takeCommand().lower()
        if "time" in query:
            time()
        elif "date" in query:
            date()
        elif "offline" in query :
            speak("getting offline ! bye "+owner)
            quit()
        elif "wiki" in query:
            wikisearch(query)
        elif "mail" in query:
            try:
                speak("what should i tell?..")
                cont="this is test mail"#takeCommand()
                to="gopimanikanta50@gmail.com"
                sendmail(to,cont)
                speak("email sent successfully")
            except Exception as e:
                speak(e)
                print(e)
        elif "picture" in query:
            takepicture()
        elif "shutdown" in query:
            os.system("shutdown /s /t 1")
        elif "logout" in query:
            os.system("shutdown -1")
        elif "restart" in query:
            os.system("shutdown /r /t 1")
        elif "songs" in query:
            playsongs()
        elif "screenshot" in query:
            speak("taking screenshot")
            screenshot()
        elif "battery" in query:
            battery()
        elif "cpu" in query:
            cpu()
        elif "joke" in query:
            joke()
                
