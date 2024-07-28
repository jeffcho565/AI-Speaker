from gtts import gTTS
from playsound import playsound

# TTS(Text to Speech)
# Text-to-Speech (TTS) is a technology that converts written text into spoken words. 
# This technology allows computers or devices to “read” text aloud, 
# making it accessible to users in an audio format. 


# 1. English
text = 'How can I help you?'
file_name = 'sample.mp3' # The audio should be saved as a file in a format like MP3 file.
tts_en = gTTS(text=text, lang='en') # we will use gTTs to convert text to speech.
tts_en.save(file_name) # use a save method to save file_name
playsound(file_name) #using playsound, you can directly read and play mp3 files within the source code. 
                       #syntax is really simple. playsound(file name)


# 2. Korean
# file_name = 'sample1.mp3'
# text = '안녕하세요. 저는 파이썬을 배우고 있습니다'
# tts_ko = gTTS(text=text, lang='ko')
# tts_ko.save(file_name)
# playsound(file_name)


# we will create a long sentence, put the content to be coverted
# into speech into that file, and then write code to read it directly.
# Make a sample.txt first. 

# file_name = 'sample.mp3'
# with open('sample.txt','r') as f:
#     text = f.read()
    
# tts_en = gTTS(text=text, lang='en')
# tts_en.save(file_name)
