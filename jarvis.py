import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib
from tkinter import*
from PIL import ImageTk,Image

root = Tk()
root.geometry("282x248")
root.title("Voice Assistant")
photo=ImageTk.PhotoImage(Image.open("2.jpg"))

def submit():
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    engine.setProperty('voice',voices[0])
    def speak(audio):
        engine.say(audio)
        engine.runAndWait()

    def wishMe():
        hour = int(datetime.datetime.now().hour)
        if hour>=0 and hour<12:
            speak("Good Morning dude!")

        elif hour>=12 and hour<18:
            speak("Good Afternoon dude!")

        else:
            speak("Good Evening dude!")

        speak("coco here, how can i help you") 

    def takeCommand():
        """
        it takes microphone input from the user and returns a string output
        """
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("listning...")
            r.pause_threshold = 1
            audio = r.listen(source)

        try:
            print("Recognizing...")
            querry = r.recognize_google(audio,language='en-in')
            print(f"user said: {querry}\n")

        except Exception as e:
            # print(e)
            print("say that again please...")
            return "None"
        return querry

    def sendEmail(to,content):
        server = smtplib.SMTP('smtp.gmail.com',587)
        server.ehlo()
        server.starttls()
        server.login('yashwanthhn76@gmail.com','*****')
        server.sendmail('yashwanthhn76@gmail.com', to, content)
        server.close() 


    if __name__ == "__main__":
        wishMe()  
        #while(True):
        if 1:
            querry = takeCommand().lower()

            # logic for executing tasks based on querry
            if 'wikipedia' in querry:
                speak("searching wikipedia...")
                querry = querry.replace("wikipedia", "")
                results = wikipedia.summary(querry,sentences=2)
                speak("According to wikipedia")
                print(results)
                speak(results)

            elif 'open youtube' in querry:
                webbrowser.open("youtube.com")

            elif 'open google' in querry:
                webbrowser.open("google.com")

            elif 'open stackoverflow' in querry:
                webbrowser.open("stackoverflow.com")

            elif 'play music' in querry:
                music_dir = 'C:\\Users\\user\\Music'
                songs = os.listdir(music_dir)
                # print(songs)
                os.startfile(os.path.join(music_dir,songs[1]))



            elif 'the time' in querry:
               strTime =  datetime.datetime.now().strftime("%H:%M:%S")
               speak(f"sir, the time is {strTime} ")

            elif 'open code' in querry:
                codepath = "C:\\Users\\user\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
                os.startfile(codepath)

            elif 'email to yashwant' in querry:
                try:
                    speak("what should i say?")
                    content = takeCommand()
                    to = "yashwanthhn76@gmail.com"
                    sendEmail(to,content) 
                    speak("email has been sent")
                except Exception as e:
                    print(e)
                    speak("sorry friend, I am not able to send your mail")
                    
speaker_label=Label(image=photo,bg="red",fg="blue")
speaker_label.pack()

my_label=Label(root,text="Tap to Speak")
my_label.pack()
my_button=Button(root,text="speak",command=submit)
my_button.pack()
root.mainloop()
