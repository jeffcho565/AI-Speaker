import speech_recognition as sr
from gtts import gTTS
from playsound import playsound
import os
import datetime

def speach(file_name):
    with open(file_name, 'r') as file:
        text = file.read()
    mp3_file = 'sample.mp3'
    tts_en = gTTS(text=text, lang='en')
    tts_en.save(mp3_file)
    playsound(mp3_file)
    os.remove(mp3_file)
        

def record():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)
    try:
        text = r.recognize_google(audio, language='en-US')
        print("[User]: %s" % text)
        with open("sample.txt", "w") as file:
            file.write(text)
        return text
    except sr.UnknownValueError:
        print("Recognition Failed")
        return ""
    except sr.RequestError as e:
        print("Request Failed: {0}".format(e))
        return ""
        
def ai_answer():

    with open("sample.txt", "r") as file:
        text = file.read()
    if text == "what is the date and time":
        text="the date and time is: %s"%(datetime.datetime.now().strftime("%m/%d/%Y %H:%M:%S"))
        print (text)
        os.remove("sample.txt")
        with open("sample.txt", "w") as file:
            file.write(f"the date and time is: {datetime.datetime.now().strftime("%m/%d/%Y %H:%M:%S")}")
        speach("sample.txt")
        os.remove("sample.txt")
    else:
        with open("ai_question.txt", "w") as file:
            file.write("How can i help you further?")
            print("[Ai]: How can i help you further?")
        speach("ai_question.txt")
     
def main():
    while True:
        user_input = record()
        if user_input == "close":
            print("[Ai]: Goodbye")
            break
        elif user_input:
            ai_answer()
main()