import speech_recognition as sr
from bot import Bot


bot = Bot()
bot.talk('Hola Buen día ¿Qué puedo hacer por ti?')
rec = bot.listen()

if "reproduce" in rec:
    print('Me dijiste que reprodujera algo')
""" try:
    # Try to get the voice from the microphone: 
    with sr.Microphone() as source:
        voice = listener.listen(source)
        # Use whisper API
        rec = listener.recognize_whisper(voice)
        print(rec)
except Exception as e:
    raise e """
# end try