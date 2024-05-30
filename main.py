import speech_recognition as sr
from bot import Bot
from functions import Duty, Detection
import pywhatkit as pwk
import datetime

exit_bot = False;
welcome_message = False
bot = Bot()
duty = Duty()
detection = Detection()


while not exit_bot:
    if not welcome_message:
        bot.talk('Hola ¿Qué puedo hacer por ti?')
        welcome_message = True
    else:
        bot.talk('¿Algo más en qué pueda ayudarte?')    
    rec = bot.listen()
    duty.main_duty(rec)
    exit_bot = detection.detect_exit(rec)
