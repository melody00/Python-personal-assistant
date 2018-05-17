import wikipedia
import webbrowser
import requests
from gtts import gTTS
from bs4 import BeautifulSoup
import os
def say(text):
        
         tts=gTTS(text=text, lang='en')
         
         tts.save("saaa.mp3")
         os.system("mpg321 saaa.mp3")
def wiki(str):
    try:
        #result = wikipedia.summary(str, sentences=2)
        url = "http://en.wikipedia.org/w/index.php?title="
        url=url+str
        r=requests.get(url)
        soup = BeautifulSoup(r.content)
        g_data=soup.find_all("p")
        result= g_data[0].text
        print(result)
        result="wikipedia says "+result
        say (result)
    except wikipedia.exceptions.PageError:
        url1 = "http://www.google.com/search?q="
        url1=url1+str
        r=requests.get(url)
        soup = BeautifulSoup(r.content)
        g_data1=soup.find_all("span",{"class":"st"})
        result= g_data[0].texts
        print (result)
        say (result)
        