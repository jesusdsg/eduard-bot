import pyttsx3
import speech_recognition as sr

engine = pyttsx3.init()
voices = engine.getProperty('voices')
""" for index, voice in enumerate(voices, start=0):
    print('Voz ', voice.id, ' index ', index) """


# Creating the listener
listener = sr.Recognizer()


class Bot:
    def talk(self, message):
        engine.setProperty('voice', voices[21].id)
        engine.say(message)
        engine.runAndWait()

    def listen(self):
        try:
            # Try to get the voice from the microphone: 
            with sr.Microphone() as source:
                voice = listener.listen(source)
                # Use whisper API
                rec = listener.recognize_whisper(voice)
                print('Record is ==>  ', rec)
                return rec
        except Exception as e:
            raise e    

