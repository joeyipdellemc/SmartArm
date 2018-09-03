import pyttsx3
engine = pyttsx3.init()
voices = engine.getProperty('voices')
# Ralph 45  Trinoidscp 54 Fred 21
rate = engine.getProperty('rate')
#engine.setProperty('rate', rate-500)
engine.setProperty('voice', voices[21].id)
engine.say('Your are under arrest.')
engine.runAndWait()
