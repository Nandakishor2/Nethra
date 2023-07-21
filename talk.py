import pyttsx3
class speaker():
    def __init__(self) :
        self.engine = pyttsx3.init()
        
    def speak(self,cmd):
        voices =self. engine.getProperty('voices')
        newVoiceRate = 145
        self.engine.setProperty('rate',newVoiceRate)
        self.engine.setProperty('voice', voices[1].id)
        self.engine.say(cmd)
        self.engine.runAndWait()



