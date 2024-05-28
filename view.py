import speech_recognition as sr
from bot import Bot
import pywhatkit as pwk


bot = Bot()
bot.talk('Hola Buen día ¿Qué puedo hacer por ti?')
rec = bot.listen()

if "reproduce" in rec:
    music_query = rec.replace("reproduce", '')
    bot.talk('Reproduciendo ' + music_query)
    pwk.playonyt(music_query)
