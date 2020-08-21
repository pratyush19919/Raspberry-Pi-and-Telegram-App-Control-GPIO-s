import telepot
import time,datetime
import RPi.GPIO as GPIO
from telepot.loop import MessageLoop

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
    chat_id=msg["chat"]["id"]
    command=msg["text"]
    print('Received: %s' % command)
    print(msg["chat"]["id"])
    if "date" in command:
        message="The Date is "+str(datetime.datetime.now().strftime("%d/%m/%Y"))
        telegram_bot.sendMessage(chat_id,message)
        


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

        telegram_bot.sendMessage(chat_id, message)


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

telegram_bot=telepot.Bot("1247076443:AAEjJ8YC0rz4ASy3d_fPmQAJF7q3RPniO4Y")
print(telegram_bot.getMe())

MessageLoop(telegram_bot,action).run_as_thread()
print("started and running")



while True:
    time.sleep(1000)

