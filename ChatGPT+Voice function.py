import openai
import speech_recognition as sr
import pyttsx3
from gtts import gTTS
import os
#Openai gives access to chatgpt, speechrecognition is selfexplanatory, pyttsx3 and gtts convert text to speech
#For some reason i cannot import the other files in the same directory that's why everything is in here
#The code is written by myself, but it is inspired by some projects from "neural9" which is a youtuber

openai.api_key = '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'  # Replace with your OpenAI API key
language = 'en'

Num = 0
#makes an mp3 file of the read text and plays it
# The error is it cannot access "Num" bacause it it is not associated with a value
def SpeakNice(Text):
    global Num
    myobj = gTTS(text=Text, lang=language, slow=False)
    myobj.save(f"speak{Num}.mp3")
    os.system(f"speak{Num}.mp3")
    Num += 1
    print(Num)

def main():
    while True:
        query = listen()
        if query:
            response = get_chatgpt_response(query)
            print(f"Assistant: {response}")
            SpeakNice(response)


engine = pyttsx3.init()


# Define a function to speak the response
def speak(response):
    engine.say(response)
    engine.runAndWait()

def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-US')
        print(f"User: {query}")
        return query
    except Exception as e:
        print("Sorry, I couldn't understand. Can you please repeat?")
        return None

def get_chatgpt_response(query):
    response = openai.Completion.create(
        engine='text-davinci-003',
        prompt=query,
        max_tokens=1000,
        n=1,
        stop=None,
        temperature=0.7
    )

    return response.choices[0].text.strip()

if __name__ == '__main__':
    main()
    pattern = "*.mp3"  # Replace with the pattern matching the files you want to delete
    files = [file for file in os.listdir() if file.endswith(pattern)]
    if len(files) > 0:
        for file in files:
            os.remove(file)