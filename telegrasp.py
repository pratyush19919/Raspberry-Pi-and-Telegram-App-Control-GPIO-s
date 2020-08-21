# import packages

import telepot   #To communicate with Telegram API we are going to use python library called telepot.
import time,datetime
import RPi.GPIO as GPIO
from telepot.loop import MessageLoop
#set up pins
GPIO.setmode(GPIO.BOARD)
Relay1=16
motor=10
Relay2=12

GPIO.setwarnings(False)

GPIO.setup(motor,GPIO.OUT)
GPIO.output(motor,0)

GPIO.setup(Relay1,GPIO.OUT)
GPIO.output(Relay1,0)

GPIO.setup(Relay2,GPIO.OUT)
GPIO.output(Relay2,0)

def action(msg):
    #function for decoding what is there in the message we typed in raspberry pi

    chat_id=msg["chat"]["id"]
    command=msg["text"]
    print('Received: %s' % command)
    print(msg["chat"]["id"])
    # if date is typed
    if "date" in command:
        message="The Date is "+str(datetime.datetime.now().strftime("%d/%m/%Y"))
        telegram_bot.sendMessage(chat_id,message)
        

#for on commands
    if "on" in command:
        message="Turned On"
        if "motor" in command:
            GPIO.output(motor,1)
            message=message + "motor"
        if "Relay1" in command:
            GPIO.output(Relay1,1)
            message=message + "Relay1"
        if "Relay2" in command:
            GPIO.output(Relay2,1)
            message=message + "Relay2"

        telegram_bot.sendMessage(chat_id, message) #replying to the message

#for on commands
    if "off" in command:
        message="Turned Off"
        if "motor" in command:
            GPIO.output(motor,0)
            message=message + "motor"
        if "Relay1" in command:
            GPIO.output(Relay1,0)
            message=message + "Relay1"
        if "Relay2" in command:
            GPIO.output(Relay2,0)
            message=message + "Relay2"

        telegram_bot.sendMessage(chat_id, message)

telegram_bot=telepot.Bot("*********************************************") #THIS IS WHERE YOU PASTE YOUR API TOKEN INSIDE QUOTES
print(telegram_bot.getMe())

MessageLoop(telegram_bot,action).run_as_thread()  #Looping the function 'action' 
print("started and running")



while True:
    time.sleep(1000)

