import speech_recognition as sr

# Initialize recognizer
Recognizer = sr.Recognizer()
r = sr.Recognizer()

# Define a function to capture audio and convert to text
def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 2 #Adjust the pause threshold according to your environment
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-US')
        print(f"User: {query}")
        return query
    except Exception as e:
        print(e)
        #print("Sorry, I couldn't understand. Can you please repeat?")
        return None

listen()