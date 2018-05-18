import requests
from bs4 import BeautifulSoup
from gtts import gTTS
import os
def say(text):
        
         tts=gTTS(text=text, lang='en')
         
         tts.save("saaa.mp3")
         os.system("mpg321 saaa.mp3")

def find(str):
	url="https://en.oxforddictionaries.com/definition/"+str
	r=requests.get(url)
	soup=BeautifulSoup(r.text,'html.parser')
	g_data=soup.find_all("span",{"class":"ind"})
	result=g_data[0].text
	print result
	say(result)
