import requests
from gtts import gTTS
from bs4 import BeautifulSoup
import os
def say(text):
        
         tts=gTTS(text=text, lang='en')
         
         tts.save("saaa.mp3")
         os.system("mpg321 saaa.mp3")
def forcast(str):
	url= "https://www.weather-forecast.com/locations/"+str
	r=requests.get(url)
	soup = BeautifulSoup(r.content)
	g_data=soup.find_all("p",{"class":"b-forecast__table-description-content"})
	result= g_data[0].text
	print (result)
	say (result)

def current_weather(str):
	url="http://www.google.com/search?q="+str
	r=requests.get(url)
	soup = BeautifulSoup(r.text,'html.parser')
	g_data=soup.find_all("div")
	result= g_data[26].text
	return  result
	'''res=" "
	c=1
	d=1
	e=1
	f=1
	l= len(result)
	
	for i in range (0,l):
		if(c==1):
			if(result[i]!='|'):
				res=res+result[i]
        	
            	
        	else:
        		c=0
            	
    	if (c!=1):
        	if(result[i]=='W'and result[i+1]=='i') and (c==0 and d!=0):
        		res=res+result[i]
        		d=0
            	
            	
        	if((d==0) and (result[i]!='k')):
        		res=res+result[i]

        	else:
        		break

	res= res+" kilometers per hour " 
	j=i
	for j in range(i,l):
		if(e==1):
			if(result[j]=='H'):
				res =res +result[j]
				e=0

        	else:
        		res=res+""
            	
    	if(e==0):

        	if(result[j]!='%'):
        		res =res +result[j]
            	
        	else:
        		break
            	
	res=res+" percent "

	print (res)'''






















































































	#x=j
	'''for x in range(j,l):

 		if(e==1):
 			if(result[x]=='H'):
 				res =res +result[x]
 				e=0
    		else:
    			res=res+""
        if(e==0):

    		if(result[x]!='%'):
    			res =res +result[x]
        	else:
        		return
	res=res+" percent "

	print (res)
	say(res)'''