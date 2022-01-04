from gtts import gTTS
from playsound import playsound
audio="speech.mp3"
lang='en'
txt=input("enter the text here: ")
sp=gTTS(text=txt,lang=lang,slow=False)
sp.save(audio)
playsound(audio)
