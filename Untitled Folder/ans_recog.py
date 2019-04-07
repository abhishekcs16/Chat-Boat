import speech_recognition as sr
from gtts import gTTS
from pygame import mixer
import pyttsx


#function to recognize voice
def recog():
    r = sr.Recognizer()
    with sr.Microphone() as source:
     print("Say something!")
     audio = r.listen(source)
     s=r.recognize_google(audio)
    # print s
     print("You said: " + r.recognize_google(audio))
     return s
#function to speak
def answer(str1):
     engine = pyttsx.init()

     #get the array of type of voices and setting a particular one

     voices=engine.getProperty('voices')
     count=0
     for voice in voices:
      if (count == 1):
       engine.setProperty('voice',voice.id)
       #for changing the volume of the speech
       #here i set it to the maximum one
       volume=engine.getProperty('volume')
       engine.setProperty('volume',volume-.00)

       #for changing rate of the speech
       rate = engine.getProperty('rate')
       engine.setProperty('rate', rate-50)

       #engine.say('The quick brown fox jumped over the lazy dog.')
    
       engine.say(str1)
      count =count + 1
     
     engine.runAndWait()

a = recog()
answer(a)

