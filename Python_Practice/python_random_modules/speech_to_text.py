import speech_recognition as sr

r = sr.Recognizer()
with sr.Microphone() as source:
    print('Speak Now')
    audio = r.listen(source)
    try:
        text = r.recognize_google(audio)
        print('you told this ', text)
    except:
        print('audio is not clear')


# import library
# initiate our recognizer
# listen the source
# use recognizer to convert our speech to text