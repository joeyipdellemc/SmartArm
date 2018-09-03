

from gtts import gTTS
from playsound import playsound

#from io import BytesIO
#mp3_fp = BytesIO()


tts=gTTS(text='You are under arrest.', lang='en-uk')

tts.save('human_voice.mp3')

#tts.write_to_fp(mp3_fp)

#from playsound import playsound
#playsound('human_voice.mp3')

