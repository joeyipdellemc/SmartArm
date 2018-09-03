

from gtts import gTTS
import pygame

tts=gTTS(text='You are under arrest.', lang='en-ie')

tts.save('happybirthday.mp3')

file = 'happybirthday.mp3'
pygame.init()
pygame.mixer.init()
pygame.mixer.music.load(file)
pygame.mixer.music.play()


