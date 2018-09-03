import getopt
import numpy as np
import scipy.io.wavfile as wavfile
import math
import sys
from waveshaper import Waveshaper
import time
import pyglet
import os
from pydub import AudioSegment

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = '\\Users\\yipj1\\Documents\\SmartArm\\robotVoice-b9ba10077aa4.json'
print("OS Environment")
print os.environ['GOOGLE_APPLICATION_CREDENTIALS']

"""Synthesizes speech from the input string of text or ssml.

Note: ssml must be well-formed according to:
    https://www.w3.org/TR/speech-synthesis/
"""
from google.cloud import texttospeech

# Instantiates a client
client = texttospeech.TextToSpeechClient()
voices = client.list_voices()

# Set the text input to be synthesized
synthesis_input = texttospeech.types.SynthesisInput(text="You are under arrest")

voiceName = []
# Build the voice request, select the language code ("en-US") and the ssml
# voice gender ("neutral")
for voice in voices.voices:
	# Display the voice's name. Example: tpc-vocoded
    voiceName.append(voice.name)

	
for currentVoice in voiceName:
	print currentVoice
	if currentVoice.startswith("en"): 
		# Build the voice request, select the language code ("en-US") and the ssml
		# voice gender ("neutral"
		voice = texttospeech.types.VoiceSelectionParams(
		name=currentVoice,
		language_code='en-US',
		ssml_gender=texttospeech.enums.SsmlVoiceGender.MALE)
		
		# Select the type of audio file you want returned
		audio_config = texttospeech.types.AudioConfig(audio_encoding=texttospeech.enums.AudioEncoding.MP3)
		
		# Perform the text-to-speech request on the text input with the selected
		# voice parameters and audio file type
		response = client.synthesize_speech(synthesis_input, voice, audio_config)
		
		# The response's audio_content is binary.
		with open('human_voice.mp3', 'wb') as out:
		# Write the response to the output file.
			out.write(response.audio_content)
			print('Audio content written to file "human_voice.mp3"')
			sound = AudioSegment.from_mp3("human_voice.mp3")
			sound.export("human_voice.wav", format="wav")
		


		# Diode constants (must be below 1; paper uses 0.2 and 0.4)
		VB = 0.2
		VL = 0.4

		# Controls distortion
		H = 0.5

		# Controls N samples in lookup table; probably leave this alone
		LOOKUP_SAMPLES = 1024

		# Frequency (in Hz) of modulating frequency
		MOD_F = 70

		def diode_lookup(n_samples):
			result = np.zeros((n_samples,))
			for i in range(0, n_samples):
				v = float(i - float(n_samples)/2)/(n_samples/2)
				v = abs(v)
				if v < VB:
					result[i] = 0
				elif VB < v <= VL:
					result[i] = H * ((v - VB)**2)/(2*VL - 2*VB)
				else:
					result[i] = H*v - H*VL + (H*(VL-VB)**2)/(2*VL-2*VB)

			return result

		def raw_diode(signal):
			result = np.zeros(signal.shape)
			for i in range(0, signal.shape[0]):
				v = signal[i]
				if v < VB:
					result[i] = 0
				elif VB < v <= VL:
					result[i] = H * ((v - VB)**2)/(2*VL - 2*VB)
			else:
				result[i] = H*v - H*VL + (H*(VL-VB)**2)/(2*VL-2*VB)
			return result

		if __name__ == "__main__":

			rate, data = wavfile.read('human_voice.wav')
			
			if len(data.shape) > 1:
				data = data[:,1]
			#data = data[:,1]

			# get max value to scale to original volume at the end
			scaler = np.max(np.abs(data))

			# Normalize to floats in range -1.0 < data < 1.0
			data = data.astype(np.float)/scaler

			# Length of array (number of samples)
			n_samples = data.shape[0]

			# Create the lookup table for simulating the diode.
			d_lookup = diode_lookup(LOOKUP_SAMPLES)
			diode = Waveshaper(d_lookup)

			# Simulate sine wave of frequency MOD_F (in Hz)
			tone = np.arange(n_samples)
			tone = np.sin(2*np.pi*tone*MOD_F/rate)

			# Gain tone by 1/3
			tone = tone * 2

			# Junctions here
			tone2 = tone.copy() # to top path
			data2 = data.copy() # to bottom path

			# Invert tone, sum paths
			tone = -tone + data2 # bottom path
			data = data + tone2 #top path

			#top
			data = diode.transform(data) + diode.transform(-data)

			#bottom
			tone = diode.transform(tone) + diode.transform(-tone)

			result = data - tone

			#scale to +-1.0
			result /= np.max(np.abs(result))
			#now scale to max value of input file.
			result *= scaler
			# wavfile.write wants ints between +-5000; hence the cast
			wavfile.write('robot_voice.wav', rate, result.astype(np.int16))
			#Play Voice
			outputVoice = pyglet.media.load('robot_voice.wav', streaming=False)
			outputVoice.play()
			time.sleep(2)
