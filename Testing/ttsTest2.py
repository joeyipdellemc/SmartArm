import pyttsx3
engine = pyttsx3.init()
voices = engine.getProperty('voices')
i=0
for voice in voices:
   engine.setProperty('voice', voice.id)
   engine.say('Your are under arrest.')
   engine.runAndWait()
   print(i)
   print(voice)
   i+= 1
