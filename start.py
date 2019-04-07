import aiml
import os
import sys
import pyttsx
from chatterbot import ChatBot
import speech_recognition as sr



def recog():
    r = sr.Recognizer()
    with sr.Microphone() as source:
     print("Say something!")
     audio = r.listen(source)
     s=r.recognize_google(audio)
    # print s
     print("You said: " + r.recognize_google(audio))
     return s

def speak(audioString):
    engine = pyttsx.init()
    engine.say(audioString)
    engine.runAndWait()

# AIML  

kernel = aiml.Kernel()

if os.path.isfile("bot_brain.brn"):
    kernel.bootstrap(brainFile = "bot_brain.brn")
else:
    kernel.bootstrap(learnFiles = "std-startup.xml", commands = "load aiml b")
    kernel.saveBrain("bot_brain.brn")

# kernel now ready for use

while True:
    cmd = raw_input("You:")
    response = kernel.respond(cmd)
    print "Castiel :"+response
    speak(response)
