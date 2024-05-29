import pywhatkit as pwk
import datetime
from bot import Bot

bot = Bot()


class Functions:
    def detect_play(self, rec):
        if "reproduce" in rec:
            music_query = rec.replace("reproduce", '')
            bot.talk('Reproduciendo ' + music_query)
            pwk.playonyt(music_query)

    def detect_time(self, rec):
        if "hora" in rec:
            time = datetime.datetime.now().strftime("%H:%M:%S")
            bot.talk("La hora es " + time)        

    def detect_exit(self, rec):
        if "salir" in rec:
            bot.talk('Fue un placer ayudarte, hasta otra')
            return True
        return False    