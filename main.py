import speech_recognition as sr
from bot import Bot
from functions import Functions
import pywhatkit as pwk
import datetime

exit_bot = False;
welcome_message = False
bot = Bot()
functions = Functions()


while not exit_bot:
    if not welcome_message:
        bot.talk('Hola ¿Qué puedo hacer por ti?')
        welcome_message = True
    else:
        bot.talk('¿Algo más en qué pueda ayudarte?')    
    rec = bot.listen()
    functions.detect_play(rec)
    functions.detect_time(rec)
    exit_bot = functions.detect_exit(rec)
