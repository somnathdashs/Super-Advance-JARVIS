import speech_recognition as sr
import pyttsx3
import meta_ai_api

class JARVIS_AI():
    def __init__(self):
        pass

    def speak(self, text):
        engine = pyttsx3.init()
        print("JARVIS: "+text)
        engine.say(text)
        engine.runAndWait()

    def listen(self):
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening...")
            audio = r.listen(source)
            try:
                command = r.recognize_google(audio)
                print("You said: " + command)
                return command
            except sr.UnknownValueError:
                print("Sorry, I did not understand that.")
                return None
            except sr.RequestError as e:
                print("Could not request results; {0}".format(e))
                return None
            except sr.WaitTimeoutError:
                print("Listening timed out while waiting for phrase to start")
                return None
    

    def get_response(self, prompt): 
        self.speak(prompt)
        pass
