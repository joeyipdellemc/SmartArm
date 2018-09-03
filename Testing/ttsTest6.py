


from playsound import playsound
import os

# Mac
#os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = '/Users/joe/Documents/SmartArm/robotVoice-b9ba10077aa4.json'
# Windows
#os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = "C:\Users\yipj1\Documents\SmartArm\robotVoice-b9ba10077aa4.json"

"""Synthesizes speech from the input string of text or ssml.

Note: ssml must be well-formed according to:
    https://www.w3.org/TR/speech-synthesis/
"""
from google.cloud import texttospeech

# Instantiates a client
client = texttospeech.TextToSpeechClient()

# Set the text input to be synthesized
synthesis_input = texttospeech.types.SynthesisInput(text="Hello, World!")

# Build the voice request, select the language code ("en-US") and the ssml
# voice gender ("neutral")
voice = texttospeech.types.VoiceSelectionParams(
	name='en-US-Standard-D',
    language_code='en-US',
    ssml_gender=texttospeech.enums.SsmlVoiceGender.MALE)

# Select the type of audio file you want returned
audio_config = texttospeech.types.AudioConfig(
    audio_encoding=texttospeech.enums.AudioEncoding.MP3)

# Perform the text-to-speech request on the text input with the selected
# voice parameters and audio file type
response = client.synthesize_speech(synthesis_input, voice, audio_config)

# The response's audio_content is binary.
with open('output.mp3', 'wb') as out:
    # Write the response to the output file.
    out.write(response.audio_content)
    print('Audio content written to file "output.mp3"')


#tts.write_to_fp(mp3_fp)


playsound('output.mp3')

