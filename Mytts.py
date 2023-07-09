from gtts import gTTS
from langdetect import detect
from playsound import playsound
import os

fileName = 'Voice.mp3'
def PlayNarration(text):
    voice = gTTS(text, lang=detect(text))
    voice.save(fileName)
    playsound(fileName)
    os.remove(fileName)