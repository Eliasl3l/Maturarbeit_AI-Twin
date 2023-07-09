from languageProcessing import get_chatgpt_response
from SpeechToText import listen
from TextToVideo import 


def main():
    while True:
        query = listen()
        if query:
            response = get_chatgpt_response(query)
            print(f"Assistant: {response}")
            SpeakNice(response)