import pyttsx3
import speech_recognition as sr

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[20].id) #Spanish language setted in voice

# Creating the listener
listener = sr.Recognizer()


class Bot:
    def talk(self, message):
        engine.say(message)
        engine.runAndWait()

    def listen(self):
        try:
            # Try to get the voice from the microphone: 
            with sr.Microphone() as source:
                voice = listener.listen(source)
                # Use whisper API
                rec = listener.recognize_whisper(voice)
                return rec
        except Exception as e:
            raise e    

