

from gtts import gTTS
import pyglet

tts=gTTS(text='You are under arrest.', lang='en-ie')

tts.save('happybirthday.mp3')


song = pyglet.media.load('happybirthday.mp3')
song.play()
pyglet.app.run()

