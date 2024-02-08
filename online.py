import pywhatkit as kit
import requests
import wikipedia
from email.message import EmailMessage
import smtplib
from decouple import config

EMAIL = "warchallenger2710@gmail.com"
PASSWORD = "wtnfqzatalckvnlh" # you have add passkey not the password. You can find it at account setting section. 

def find_my_ip():
    ip_address = requests.get('https://api.ipify.org?format=json').json()
    return ip_address['ip']

def search_on_wikipedia(query):
    results = wikipedia.summary(query, sentences = 2)
    return results

def search_on_google(query):
    kit.search(query)

def youtube(video):
    kit.playonyt(video)

# def send_email(receiver_add, subject, body):
#     try:
#         email = EmailMessage()
#         email['To'] = receiver_add
#         email['Subject'] = subject
#         email['From'] = EMAIL

#         email.set_content(body)
#         s = smtplib.SMTP("smtp.gmail.com",587)
#         s.starttls()
#         s.login(EMAIL, PASSWORD)
#         s.send_message(email)
#         s.close()

#         return True
    
#     except Exception as e:
#         print(e)
#         return False
    
def get_news():
    headline = []
    result = requests.get(f"https://newsapi.org/v2/top-headlines?country=in&category=general&apiKey=909dcc3816f04ccc80974ffa4135d5c5").json()
    # you can change the type of news and country here if needed
    articles = result["articles"]
    for article in articles:
        headline.append(article["title"])
    return headline[:6]

# def weather_forcast():
#     res = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q=ahmedabad&appid=572ef6f316176be9e79804b83afddf41").json()
#     #you can change the city as you want
#     print(res)

#     if "weather" in res and res["weather"]:
#         weather = res["weather"][0]["main"]
#     else:
#         weather = "Not available"

#     if "main" in res:
#         temp = res["main"].get("temp", "Not available")
#         feels_like = res["main"].get("feels_like", "Not available")
#     else:
#         temp, feels_like = "Not available", "Not available"

#     return weather, f"{temp}°f", f"{feels_like}°f"


