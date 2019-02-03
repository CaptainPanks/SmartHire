import speech_recognition as sr  
import os
from pydub.silence import split_on_silence
from pydub import AudioSegment


'''   
# obtain audio from the microphone  
r = sr.Recognizer()  
with sr.Microphone() as source:  
  print("Please wait. Calibrating microphone...")  
  # listen for 5 seconds and create the ambient noise energy level  
  r.adjust_for_ambient_noise(source, duration=5)  
  print("Say something!")  
  audio = r.listen(source)  
   
# recognize speech using Sphinx  
try:  
  print("Sphinx thinks you said '" + r.recognize_sphinx(audio) + "'")  
except sr.UnknownValueError:  
  print("Sphinx could not understand audio")  
except sr.RequestError as e:  
  print("Sphinx error; {0}".format(e))  
'''


sound = AudioSegment.from_file("test.wav", format="wav")
chunks = split_on_silence(sound, min_silence_len=700, silence_thresh=-30, keep_silence=200)

r = sr.Recognizer()

print(len(chunks))

for i in range(len(chunks)):
	filename = 'chunk'+str(i)+'.wav'
	chunks[i].export(filename, format ="wav") 
	with sr.AudioFile(filename) as source:
    		audio = r.record(source)
	speech = r.recognize_sphinx(audio)
	print(speech)
	os.remove(filename)
