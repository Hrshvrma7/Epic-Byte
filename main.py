import pyttsx3
from datetime import datetime
import speech_recognition as sr
from random import choice
from conv import random_text
import keyboard
import os
import subprocess as sp
from online import find_my_ip,search_on_google,search_on_wikipedia,youtube,get_news
import requests
from bs4 import  BeautifulSoup
import imdb
import wolframalpha



engine = pyttsx3.init('sapi5')
engine.setProperty('volume',1.5)
engine.setProperty('rate',180)
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)

def speak(text):
    engine.say(text)
    engine.runAndWait()

def greet_me():
    hour = datetime.now().hour
    if (hour>=6) and (hour<12):
        speak(f"Good Morning Sir!")
    
    elif (hour>=12) and (hour<16):
        speak(f"Good Afternoon Sir!")
    
    elif (hour>=16) and (hour<=19):
        speak(f"Good Evening Sir!")
    
    speak(f"I am your assistant Epic Byte")
    speak(f"How may I help you sir?")

Listening = False

def start_listening():
    global Listening
    Listening = True
    print("Started listening")

def pause_listening():
    global Listening
    Listening = False
    print("Stopped listening")

keyboard.add_hotkey('ctrl+alt+k',start_listening)
keyboard.add_hotkey('ctrl+alt+p',pause_listening)


def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        query = r.recognize_google(audio,language= 'en-in')
        print(f"User said : {query}\n")
        if not 'bye' in query or 'exit' in query:
            response = choice(random_text)
            print(f"Epic Byte said: {response}")
            speak(response)
            
        else:
            hour = datetime.now().hour
            if hour >=21 and hour < 6:
                speak("Good night Sir. Have a good sleep.")
            else:
                speak("Have a good day Sir! See you soon.")
            exit()

    except Exception:
        speak("Sorry I couldn't understand. Can you please repeat that?" or "I see that you are busy. Can I help you with something else?")
        query ='None'
    return query

if __name__ == "__main__":
    greet_me()
    while True:
        if Listening:
            query = take_command().lower()
            if "how are you" in query:
                speak("I am absolutely fine Sir. What's about you?")

            elif "open command prompt" in query:
                speak("Opening command prompt")
                os.system('start cmd')

            elif "open camera" in query:
                speak("Opening the Camera")
                sp.run('start microsoft.windows.camera:',shell=True)
            
            elif "open notepad" in query:
                speak("Opening Notepad")
                notepad_path = "C:\\Windows\\notepad.exe"
                os.startfile(notepad_path)

            elif "ip address" in query:
                ip_address = find_my_ip()
                speak(f"Your IP Address is {ip_address}.")
                print(f"Your IP Address is {ip_address}.")

            elif "youtube" in query:
                speak(f"What dou you want to play on YouTube Sir?")
                video = take_command().lower()
                youtube(video)
            
            elif "open google" in query:
                speak(f"What should I search for on Google, Sir?")
                query = take_command().lower()
                search_on_google(query)

            elif "time" in query:
                search = f"What is time now"
                url = f"https://www.google.com/search?q={search}"
                r = requests.get(url)
                data = BeautifulSoup(r.text,"html.parser")
                time = data.find("div", class_ = "BNeawe").text
                speak(f"current time is {time}")

            elif "wikipedia" in query:
                speak(f"What would you like to know, Sir?")
                search = take_command().lower()
                results = search_on_wikipedia(search)
                speak(f"Accoring to wikipedia,{results}") 
                speak("I am printing results on terminal : ")
                print(results)

            # elif "send an email" in query:
            #     speak("What should be the subject of your mail? Sir.")
            #     subject = input("Enter the Subject for your mail: ")
            #     speak("What is the message?")
            #     body = input("Enter the Body of your mail: ")
    
            #     # Manually assigning the email address in the terminal
            #     receiver_add = input("Enter the email address: ")

            #     if send_email(receiver_add,subject,body):
            #         speak("Email has been sent successfully.")
            #         print("Email has been sent successfully.")

            #     else:
            #         speak("Sorry, I am unable to send this email. Please check the error log.")

            elif "give me some news" in query:
                speak(f"I am reading out the latest headline of today, Sir.")
                speak(get_news())
                speak("I am printing it on the terminal as well, Sir.")
                print(*get_news(),sep='\n')

            # elif 'weather' in query:
            #     #ip_address = find_my_ip() 
            #     city = requests.get(f"https://ipapi.co/103.85.10.78/city").text #you can change  ip according to location from asking 'EPIC'
            #     speak(f"Getting weather information for {city} sir.")
            #     weather,temp,feels_like = weather_forcast()
            #     speak(f"The current temperature is {temp},but it feels like {feels_like}. And the forecast says {weather}.")
            #     speak(f"Also the weather report talks about {weather}")
            #     print(f"Description :{weather}\nTemperature: {temp}\nFeels Like: {feels_like}")
                
            elif "weather" in query or "temperature" in query:
                speak("Which city's temperature do you want to know?")
                city = take_command().lower()
                # city = "Ahmedabad" # you can enter any city
                search = f"temperature in {city}"
                url = f"https://www.google.com/search?q={search}"
                r = requests.get(url)
                data = BeautifulSoup(r.text,"html.parser")
                temp = data.find("div", class_ = "BNeawe").text
                speak(f"current{search} is {temp}")

            elif "movie" in query:
                movies_db = imdb.IMDb()
                speak("Tell me the movie name that you want to know. For example, tell me about Avengers.")
                text = take_command()
                movies = movies_db.search_movie(text)
                speak("searching for" + text)
                speak("I found these")
                for movie in movies:
                    title = movie["title"]
                    year = movie["year"]
                    speak(f"{title}, released in {year}.")
                    info = movie.getID()
                    movie_info = movies_db.get_movie(info)
                    rating = movie_info["rating"]
                    cast = movie_info["cast"]
                    actor = cast[0:5]
                    plot = movie_info.get('plot outline','plot summary not available')
                    speak(f"{title} was released in {year} has imdb ratings of {rating}. The "
                          f"plot summary of movie is {plot}")# It has a cast of{actor}
                    print(f"{title} was released in {year} has imdb ratings of {rating}. The "
                          f"plot summary of movie is {plot}")# It has a cast of{actor}
                    
                
            elif "calculate" in query:
                app_id = "8JVRT2-93L4EJ583Q"
                client = wolframalpha.Client(app_id)
                ind = query.lower().split().index("calculate")
                text = query.split()[ind +1:]
                result = client.query(" ".join(text))
                try:
                    ans = next(result.results).text
                    speak("The answer is " + ans)
                    print("The answer is" + ans)
                except StopIteration:
                    speak("I couldn't find that. Please try again")

            elif "what is" in query or "who is" in query or "which is" in query:
                app_id = "8JVRT2-93L4EJ583Q"
                client = wolframalpha.Client(app_id)
                try:
                    ind = query.lower().index('what is') if 'what is' in query.lower() else\
                        query.lower().index('who is') if 'who is' in query.lower() else\
                        query.lower().index('which is') if 'which is' in query.lower() else None
                    
                    if ind is not None:
                        text = query.split()[ind +1:]
                        result = client.query(" ".join(text))
                        ans = next(result.results).text
                        speak("The answer is " + ans)
                        print("The answer is : " + ans)

                    else:
                        speak("I couldn't find that.")
                
                except StopIteration:
                    speak("I couldn't find that. Please try again")