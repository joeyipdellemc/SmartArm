from pydub import AudioSegment
sound = AudioSegment.from_mp3("human_voice.mp3")
sound.export("human_voice.wav", format="wav")
