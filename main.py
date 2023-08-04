from languageProcessing import get_chatgpt_response
from SpeechToText import listen
from TextToVideo import make_video
import os

NUM = 0

def main():
    global NUM
    while True:
        query = listen()
        if query:
            response = get_chatgpt_response(query)
            print(f"Assistant: {response}")
            make_video(response, NUM)
            NUM += 1
            if NUM > 1:
                os.remove(f'output{NUM-2}.mp3')

main()