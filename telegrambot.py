#credits for code: Salman Faris
#remember to change down here the IP address of your IoT SmarTimer in line 22, 29 and 33.
#remember to insert your telegram bot API key in line 62

import sys
import time
import random
import datetime
import telepot
import os

On = "Water Heater is ON"
On1 = "Water Heater was already ON"
Off = "Water Heater is OFF"
Off1 = "Water Heater was already OFF"
default = "Usable commands: On, Off, Status. Pay attention: I'm case sensitive"

def on(pin):
	if status(1) == On: 
        	return On1
	elif status(1) == Off:
		os.system("curl \"http://192.168.1.241/method=%22get%22?SaveBtn1=Manual+Override\"")
		return On

def off(pin):
	if status(1) == Off: 
        	return Off1
	elif status(1) == On:
		os.system("curl \"http://192.168.1.241/method=%22get%22?SaveBtn1=Manual+Override\"")
		return Off

def status(pin):
		f=os.popen("curl -s \"http://192.168.1.241\" | grep Output ")
		status = f.read()
		if 'ON' in status:
			return On
		elif 'OFF' in status:
			return Off


def handle(msg):
    chat_id = msg['chat']['id']
    command = msg['text']


    print('Got command: %s' % command)

    if command == 'On':
       bot.sendMessage(chat_id, on(1))

    elif command =='Off':
       bot.sendMessage(chat_id, off(1))

    elif command =='Status':
       bot.sendMessage(chat_id, status(1))

    else:
       bot.sendMessage(chat_id, default)



bot = telepot.Bot('API_KEY_HERE')
bot.message_loop(handle)
print('I am listening...')

while 1:
    try:
        time.sleep(10)

    except KeyboardInterrupt:
        print('\n Program interrupted')
        exit()

    except:
        print('Other error or exception occurred!')
