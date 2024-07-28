# Speech-to-Text (STT), also known as speech recognition, is a technology that converts spoken language into written text. 
# This technology allows devices and applications to understand and process human speech, 
# making it possible for users to interact with them through voice commands.

import speech_recognition as sr

# This project requires a microphone. 
# Listening to audio from the microphone.
r = sr.Recognizer() # syntax 
with sr.Microphone() as source:
    print("Start")
    audio = r.listen(source) 
    # The listen function captures the audio soure from the microphone and stores the result in the variable audio. 
    # A slight delay occurs during the process, so I included the text "start"
    # When the stored audio in the audio variable is sent to Google, the server processes it and sends back 
    # the recognized speech data, allowing you to see it as text.


# Loading audio from a file
# r = sr.Recognizer()
# with sr.AudioFile('sample.wav') as source: # The types of file that can be used here somewhat limited. (wav, aiff, flac) no mp3 file
#     audio = r.record(source)



# Exception handling is a method to handle errors or exceptional situations 
# that may occur during program execution, ensuring the program does not terminate abnormally. 
# 
# In Python, exception handling is primarily implemented using the try, except, else, and finally keywords.
try:
    text = r.recognize_google(audio, language = 'en-US')
    print(text) 
    #Korean 
    # text = r.recognize_google(audio, lanuage = 'ko')
    # print(text)
except sr.UnknownValueError: # The first one is exception handling for cases where speech recognition fails like some noise.
    print("Recognition failed")
except sr.RequestError as e:
    print("Request failed : {0}".format(e)) # This case also handles errors in speech recognition, but it specifically addresses exceptions that occur due to network or internet issues.
                                            # To understand what went wrong, the error is printed as e.

