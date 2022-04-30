import googletrans
import speech_recognition as sr
import gtts
import playsound
import pyttsx3
import pywhatkit


engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

recognizer = sr.Recognizer()
microphone=sr.Microphone()

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def song():
    microphone=sr.Microphone()
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        speak('which song will you like me to play for you')
        speak('Speak Now')
        recognizer.adjust_for_ambient_noise(source)
        voice = recognizer.listen(source)
        print(voice)
        print('Recognizing your voice')
        text = recognizer.recognize_google(voice, language='en')
        print('Wait....')
        print(text)
        speak('playing song'+text)
        pywhatkit.playonyt(text)

    

def translation():
    microphone=sr.Microphone()
    recognizer = sr.Recognizer()
    translator = googletrans.Translator()
    input_lang = 'en'
    output_lang = 'hi'
    with sr.Microphone() as source:
        print('Speak Now')
        recognizer.adjust_for_ambient_noise(source)
        voice = recognizer.listen(source)
        print(voice)
        print('Recognizing your voice')
        text = recognizer.recognize_google(voice, language=input_lang)
        print('Wait....')
        print(text)
        print('translating...')

    translated = translator.translate(text, dest=output_lang)
    print(translated.text)
    converted_audio = gtts.gTTS(translated.text, lang=output_lang)
    print('saving audio')
    converted_audio.save('translate.mp3')
    print('playing audio')
    playsound.playsound('translate.mp3')

def start():
    microphone=sr.Microphone()
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print('Speak Now')
        speak('speak')
        recognizer.adjust_for_ambient_noise(source)
        voice = recognizer.listen(source)
        print(voice)
        print('Recognizing your voice')
        
        try:
            text = recognizer.recognize_google(voice, language='en')
            if (text==str('translate')):
                translation()
                start()
            elif (text==str('how are you')):
                speak("I am fine")
                start()
            elif (text==str('What is your Name') or text==str('Your Name') or text==str('name')):
                speak('My Name is KAKATONA')
                start()
            elif (text==str('Quit') or text==str('turn off') or text==str('thank you') or text==str('exit')):
                speak('Thank You Sir')
                speak('Call me whenever u need my help')
            elif (text==str('search')):
                speak('okay')
            elif (text==str('play song')):
                song()
                start()
            else:
                print(text)
                speak('searching'+text)
                pywhatkit.search(text)
                start()

        except Exception as e:
            speak("Speech not recognised")
            start()
speak('My name is KAKATONA')
start()

    
'''https://machinelearningknowledge.ai/create-ai-voice-assistant-with-speech-recognition-python-project-source-code/'''