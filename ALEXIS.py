# it is similar to 'jarvis' but I have given my own name ... ALEXIS
# All the comments is additional you can use it by your skills


import pyttsx3 # pip install pyttsx3
import datetime
import speech_recognition as sr # pip install SpeechRecognition
import wikipedia # pip install wikipedia
import webbrowser as wb
import os
import smtpd
import smtplib
import psutil # pip install psutil
import pyjokes
import pyautogui # pip install pyautogui
from time import sleep

engine = pyttsx3.init()
"""voices = engine.getProperty('voices')
print(voices[0].id)
engine.setProperty("voices", voices[0].id)
"""
def speak(audio):
    '''
    will make ALIXIS speak
    '''
    engine.say(audio)
    engine.runAndWait()


def aboutALEXIS():
    '''
    telling about his creater 
    (you can add more to it if you want)
    '''
    speak('dear sir, my name is ALEXIS;'
    'one type of personal assistace ,;'
    'i can help you in as many way you allow me to do;'
    'i am created by one genius person names niramay thakar;'
    'it can be also said that niramay thakar is my creator')


def SpellingALEXIS():
    '''
    it will print the spelling on console and also speak the spelling
    of his name whenever you will ask for
    '''
    speak ("Spelling of my name is ... ")
    print("Spelling of my name is\n")
    print("       ||       ")
    print("       \/         ")
    print("\n :-- ALEXIS --: \n")
    speak("A,; L,; E,; X,; I,; S")
    speak("alexis")
    


def date():
    '''
    tell me the date whenever i will ask for
    '''
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    date = int(datetime.datetime.now().day)
    speak("dear sir, the current date is")
    speak(date)
    speak(month)
    speak(year)


def time():
    '''
    tell me the time whenever i will ask for
    '''
    Time = datetime.datetime.now().strftime("%I:%M:%S")
    speak("dear sir, the current time is")
    speak(Time)


def wishme():
    """
    it will wish me as we start it
    """

    speak("Welcome back sir!")
    speak("i am ALIXIS, your personal assistance ... ")
    
    """speak("how are you sir ... ")
    Iam = takeCommand().lower

    if 'i am fine' in Iam:
        speak("That's great i am happy to know that you are fine..")
    elif 'how are you' in Iam:
        speak("i am also fine because you are fine")
    
    elif 'i am not fine' in Iam:
        speak("why what happened sir, can i help you ?")
        if 'no nothing' or "no you can't" in Iam:
            speak("as you wish sir")
            if 'how are you' in Iam:
                speak("i am also not fine because you are not fine")
    time()
    date()"""

    hour = datetime.datetime.now().hour
    if hour >= 6 and hour<12:
        speak("Good morning sir!")
    elif hour >=12 and hour<18:
        speak("Good afternoon sir")
    elif hour >= 18 and hour<24:
        speak("Good Evening sir")
    else:
        speak("Good night sir")

    #speak("I am ALEXIS, your personal assistance ...")
    speak("Please tell me how can i help you ..?")



def takeCommand():
    '''
    It takes microphone input from user 
    '''

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listing ... ")
        r.pause_threshold = 1
        audio = r.listen(source)
        
    try:
        print("Recognizing ... ")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said ->>  {query}\n")

    except Exception as e:
        print(e)

        print("plz repeat")
        speak("Can you please say it again ... ")
        return "None"
    return query


def sendEmail(to, content):
    '''
    will help you to send email
    '''
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gamil.com', '123')
    server.sendmail('youremail@gmail.com', to, content)
    server.close()


def cpu():
    '''
    will show your system detail
    '''
    usage = str(psutil.cpu_percent())
    speak('CPU is at'+ usage)
    battery = psutil.sensors_battery()
    speak("Battery is at")
    speak(battery.percent )


def jokes():
    speak(pyjokes.get_joke())


def screenshot():
    img = pyautogui.screenshot()
    img.save("This Pc\\Pictures")


if __name__ == "__main__":
    wishme()
    while True:
        query = takeCommand().lower()
        
        #Logic to execute task based on query ..
        if 'wikipedia' in query:
            speak("Searching Wikipedia .... ")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=3)
            speak("Accourding to wikipedia :- \n")
            print(results)
            speak(results)
 

        elif 'my device status' in query:
            usage = str(psutil.cpu_percent())
            usage = str(psutil.cpu_percent())
            speak('CPU is at'+ usage)
            battery = psutil.sensors_battery()
            speak("Battery is at")
            speak(battery.percent )

        
        elif 'wait a minute' in query:
            speak("Ok sir ... ")
            speak("I'll be back in 10 second .. ")
            sleep(10)

        elif 'joke' in query:
            speak(pyjokes.get_joke())

        elif 'open youtube' in query:
            wb.open("youtube.com")
        elif 'open google' in query:
            wb.open("google.com")
        elif 'open instagram' in query:
            wb.open("instagram.com")


        elif 'about yourself' in query:
            speak("Yes, offcouse")
            sleep(1)
            aboutALEXIS()
        elif "your spelling" in query:
            speak("Sure, just wait a moment please")
            SpellingALEXIS()
            speak("you can also see it on your console, if you want to see spelling of my name")


        elif 'play music' in query:
            music_dir = 'C:\\Users\\91830\\Music'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))

        
        elif 'the time' in query:
            time()
        elif 'the date' in query:
            date()


        elif 'open vs code file' in query:
            #codePath = "D:\\VS CODE NIRAMAY"
            codePath = "C:\\Users\\91830\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Visual Studio Code"
            os.startfile(codePath)

        
        elif 'send email to Hemang' in query:
            try:
                speak("what do you want to say ..??")
                content = takeCommand()
                to = "hemangyourEmail@gmail.com"
                sendEmail(to,content)
                speak("Email has been sent")
            except Exception as e:
                print(e)
                speak("Sorry can't send email")


        elif 'goodbye' in query:
            speak("Good Bye dear sir ")
            quit()
        elif 'thank'in query:
            speak("it's my pleasure sir ")      
        

# Few more funtions you can try ...
        
        """ elif "how are you" in query:
            speak("I'm fine sir thanks for asking ...")
            speak("How are you ..?? ")
        elif "i am fine" or 'i am also fine' in query:
            speak("Thats great, i am happy to know; that you are fine")

        
        elif 'remember that' in query:
			speak("What should I remember?")
			data = takeCommand()
			speak("you said me to remember that"+data)
			remember = open('data.txt','w')
			remember.write(data)
			remember.close()


        elif 'logout' in query:
			os.system("shutdown -l")
		
        elif 'shutdown' in query:
			os.system("shutdown /s /t 1")
        
        elif 'restart' in query:
			os.system("shutdown /r /t 1")


        elif 'Can you Search These' in query:
			speak("What should i search ..?")
			chromepath = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
			VivaldiBrowser = 'C:/sers/91830/AppData/Local/Vivaldi/Application/vivaldi.exe %s'
			BraveBrowser = 'C:/Program Files/BraveSoftware/Brave-Browser/Application/brave.exe %s'

			search = takeCommand().lower()
			wb.get(BraveBrowser).open_new_tab(search+'.com')

      elif 'joke' in query:
		      	jokes()"""
