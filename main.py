import my_speech
import time
import datetime
import gsearch
import mywiki
import myweather
import my_dictionary
from gtts import gTTS
import os
#app_id = "GWVLUE-J9A8GKRQGE"
#client = wolframalpha.Client(app_id)

def say(text):
        
         tts=gTTS(text=text, lang='en')
         
         tts.save("saaa.mp3")
         os.system("mpg321 saaa.mp3")

speech_identifier = my_speech.Recognizer()


def phrase():

        with my_speech.Microphone() as source:
                speech_identifier.adjust_for_ambient_noise(source)
                audio = speech_identifier.listen(source)

        try:
                return speech_identifier.recognize_google(audio)

        except my_speech.UnknownValueError:
                print("I'm waiting for your command")


        return ""

localtime = time.asctime( time.localtime(time.time()) )


now = datetime.datetime.now()
hr=now.hour
dic1="what is the meaning of "
dic2="tell me the meaning of "
dic3="meaning of "
dic4="search the meaning of "
google = "Google about "
google1="Gogle for "
google2="search "
search = "search for "
search1= "search about "
wiki = "Wiki about "
wiki1 = "tell me about "
wiki2 = "who is "
wiki3 = "what is an "
wiki4 = "what is a "
wiki5 = "what is the "
weather = "tell me weather forecast of "
weather7= "tell me weather of "
weather1 = "how is the weather in "
weather2= "weather in "
weather8="current weather in "
weather9="weather of "
weather10="current weather of "
weather3= "weather forecast in "
weather4= "weather forecast of "
weather5="what is weather forecast in "
weather6="what is weather forecast of "



if hr < 12:
    print("Good moring sir. Have a nice day")
    say("good moring sir. Have a nice day")
elif hr >= 12 and hr < 17:
    print("Good afternoon sir")
    say("good afternoon sir")
elif hr >= 17 and hr <= 19:
    print("Good Evening Boss")
    say("good evening boss")

say("Welcome! I'm jarvis, An Voice Assistant Artificial Intelligence And I'm ready for your service")

print("\n# Start speaking to jarvis")


while 1:

        str=phrase()

        #say(str)
        print (str)
        #mywiki.wiki(str)
        if str == "hello" or str == "hi":
                print("hello sir\n")
                say("hello sir")

        elif str == "jarvis you there" or str == "there" or str == "are you there":
                print("Yes sir, I am at your service \n")
                say("Yes sir, I am at your service ")

        elif str == "jarvis":
                print("yes sir\n")
                say("yes sir")

        elif str == "hey":
                print("sir\n")
                say("sir")

        elif str == "what time is it" or str == "tell me time" or str == "what's the time" or str == "time" or str == "what is today" or str == "what's today" :
                print(localtime +"\n")
                say(localtime)

        elif str == "you are awesome":
                print("thank you sir, it's all your credit\n")
                say("thank you sir, it's all your credit")

        elif str == "bye" or str == "buy" or str == "break" or str == "bye jarvis" or str == "brake" or str == "terminate":
                if hr >= 20 and hr <=24:
                    print("Good night sir\n")
                    say("Good night sir")
                else:
                    print("see you again sir\n")
                    say("see you again sir")
                break

        elif str == "how are you":
                print("I'm good sir. How are you?\n")
                say("I'm good sir. How are you?")

        elif str == "great" or str == "nice" or str == "fine" or str == "good" or str == "ok" or str == "okay" or str == "alright" or str == "cool":
                print("sir\n")
                say("sir")
        elif str== dic1+str[23:] or str==dic2+str[23:]:
            my_dictionary.find(str[23:])

        elif str== dic3+str[11:]:
            my_dictionary.find(str[11:])

        elif str== dic4+str[22:]:
            my_dictionary.find(str[22:])


        elif str == google+str[13:] or str==search1+str[13:] :
            print("here we go")
            gsearch.search(str[13:])
            mywiki.wiki(str[13:])

        elif str == search+str[11:] or str== google1+str[11:] :
            print("I'm on it sir")
            gsearch.search(str[11:])
            mywiki.wiki(str[11:])

        elif str==google2+str[7:]:
            gsearch.search(str[7:])
            mywiki.wiki(str[7:])

        elif str == wiki+str[11:] :
            #say("yes sir")
            mywiki.wiki(str[11:])

        elif str == wiki1+str[14:] :
            mywiki.wiki(str[14:])

        elif str == wiki2+str[7:] :
            mywiki.wiki(str[7:])

        elif str == wiki3+str[11:] :
            mywiki.wiki(str[11:])


        elif str == wiki4+str[10:] :
           mywiki.wiki(str[10:])

        elif str==wiki5+str[11:] :
            mywiki.wiki(str[11:])


        elif str == weather+str[28:] :
            myweather.forecast(str[28:])

        elif str == weather3+str[20:] :
            myweather.forecast(str[20:])
           

        elif str == weather4+str[20:] :
            myweather.forecast(str[20:])
            

        elif str == weather5+str[28:]:
            myweather.forecast(str[28:])
            

        elif str == weather6+str[28:]:
            myweather.forecast(str[28:])
        
        elif str==weather7+str[19:] or str==weather1+str[21:] or str==weather2+str[11:] or str==weather8+str[19:] or str==weather9+str[11:] or str==weather10+str[19:] :
            print str
            result=myweather.current_weather(str)
            res=" "
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
                
                
                    if((d==0) and(result[i]!='k' and result[i]!='W')):
                        res=res+result[i]

                    elif(result[i]=='k'):
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

            print (res)

        else:
            if(str!=""):
                try:
                    gsearch.calc(str)

                except:
                    mywiki.wiki(str)
                    gsearch.search(str)
                    
            else:
                print("Sorry, I didn't get you")
                say("Sorry, I didn't get you")        

