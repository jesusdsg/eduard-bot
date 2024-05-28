import speech_recognition as sr
from bot import Bot
import pywhatkit as pwk
import datetime


bot = Bot()
bot.talk('Hola Buen día ¿Qué puedo hacer por ti?')
rec = bot.listen()

if "reproduce" in rec:
    music_query = rec.replace("reproduce", '')
    bot.talk('Reproduciendo ' + music_query)
    pwk.playonyt(music_query)

if "hora" in rec:
    time = datetime.datetime.now().strftime("%H:%M:%S")
    bot.talk("La hora es " + time)
