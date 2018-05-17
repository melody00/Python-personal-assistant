import requests
import urllib
from gtts import gTTS
from bs4 import BeautifulSoup
import os
def say(text):
        
         tts=gTTS(text=text, lang='en')
         
         tts.save("saaa.mp3")
         os.system("mpg321 saaa.mp3")

def search(str):
    url1 = "http://www.google.com/search?q="
    url1=url1+str
    r=requests.get(url1)
    soup = BeautifulSoup(r.content)
    g_data=soup.find_all("span",{"class":"st"})
    result= g_data[0].text
    print(result)
    result="google says "+ result
    say (result)
def calc(str):
    url = "http://www.google.com/search?q="+str
    r=requests.get(url)
    soup = BeautifulSoup(r.text,'html.parser')
    g_data=soup.find_all("span")
    result= g_data[4].text
    l=len(result)
    res=""
    for i in range(0,l):
        if(result[i]=='='):
            break
    
    i=i+1
      
    for j in range(i,l):
        res=res+result[j]
    

    print (res)
    res="google calculator says the answer is "+res
    
    say (res)












