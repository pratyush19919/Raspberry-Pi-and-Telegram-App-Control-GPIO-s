#import required libraries & packages
import telepot  #for telegram
import time,datetime
import RPi.GPIO as GPIO
import requests #for web-scraping
import random
from bs4 import BeautifulSoup # for parsing
from telepot.loop import MessageLoop

GPIO.setmode(GPIO.BOARD)
#setting & initializing pins
Relay1=16
led =10
Relay2=12

GPIO.setwarnings(False)

GPIO.setup(led,GPIO.OUT)
GPIO.output(led,0)

GPIO.setup(Relay1,GPIO.OUT)
GPIO.output(Relay1,0)

GPIO.setup(Relay2,GPIO.OUT)
GPIO.output(Relay2,0)


def action(msg):
    chat_id=msg["chat"]["id"] #chat_id contains the header information for message
    command=msg["text"]  #command contains the text that we write in chat
    print('Received: %s' %command)
    print(msg["chat"]["id"])
    if "date" in command:    # to get date
        message="The Date is "+str(datetime.datetime.now().strftime("%d/%m/%Y"))
        telegram_bot.sendMessage(chat_id,message)
    
    if "time" in command:   # to get time
        message="The Time is "+str(datetime.datetime.now().strftime("%H:%M:%S"))
        telegram_bot.sendMessage(chat_id,message)
    # to get top 10 headlines of news     
    if "news" in command:  # if your message containes "news" , it replies you top headlines of the day
        message="<==:::: Today's headlines are ::::==> \n"
        for i, x in enumerate(scrape()):
            message += "----------------------------\n"
            message += str(i+1) + " " + x + "\n"
        telegram_bot.sendMessage(chat_id,message)
        
# to control raspberry pi gpio's 

    if "on" in command:
        message="Turned On"
        if "Led" in command:
            GPIO.output(led,1)
            message=message + " Led"
        if "Relay1" in command:
            GPIO.output(Relay1,0)
            message=message + " Relay1"
        if "Relay2" in command:
            GPIO.output(Relay2,0)
            message=message + " Relay2"


        telegram_bot.sendMessage(chat_id, message)


    if "off" in command:
        message="Turned Off"
        if "Led" in command:
            GPIO.output(led,0)
            message=message + " Led"
        if "Relay1" in command:
            GPIO.output(Relay1,1)
            message=message + " Relay1"
        if "Relay2" in command:
            GPIO.output(Relay2,1)
            message=message + " Relay2"
        #print(chat_id)
        telegram_bot.sendMessage(chat_id, message)
        
        
def scrape():# Function for scraping the news website for getting the headlines
    news=[]
    url = "https://www.indiatoday.in/news.html"  # url of website that we want to scrape
    res=requests.get(url)
    code=BeautifulSoup(res.text,"lxml")
    head=code.find_all("p",class_="story")
    for i in range(0,10):
        news.append(str(head[random.randint(0,len(head))-1].text))
    return news #returns list of headlines in the website


telegram_bot=telepot.Bot("******************************************")#API Key you get from the bot-father in telegram app

print(telegram_bot.getMe())


MessageLoop(telegram_bot,action).run_as_thread()
print("started and running")



while True:
    time.sleep(1000)

