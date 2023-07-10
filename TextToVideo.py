from elevenlabs import generate, play, set_api_key
from elevenlabs.api import History
import requests
import pyttsx3
import pygame
engine = pyttsx3.init()
playaudio = pygame.mixer.init()
#https://docs.elevenlabs.io/api-reference/quick-start/introduction  for Documentation
#https://github.com/elevenlabs/elevenlabs-python/tree/main  Github Page
set_api_key("67f3b63436afb1d0a558a87d22d05a40")

skip_on_failure=True


#Code is copied from the elevenlabs https://docs.elevenlabs.io/api-reference/text-to-speech-stream and then edited to my purposes
CHUNK_SIZE = 6024
url = "https://api.elevenlabs.io/v1/text-to-speech/21m00Tcm4TlvDq8ikWAM"

headers = {
  "Accept": "audio/mpeg",
  "Content-Type": "application/json",
  "xi-api-key": "67f3b63436afb1d0a558a87d22d05a40"
}



def Speak(TEXT, NUM):
    global data
    global audio
    data = {
    "text": TEXT,
    "model_id": "eleven_monolingual_v1",
    "voice_settings": {
    "stability": 0.5,
    "similarity_boost": 0.5
      }
    }
    response = requests.post(url, json=data, headers=headers)
    with open(f'output{NUM}.mp3', 'wb') as f:
          for chunk in response.iter_content(chunk_size=CHUNK_SIZE):
                if chunk:
                     f.write(chunk)
                     #engine.say(chunk)
                     #play(chunk)
          
    pygame.mixer.music.load(f"output{NUM}.mp3") #partially from the pygame website   https://www.pygame.org/docs/
    pygame.mixer.music.play()

    # Keep the program running until the song ends
    while pygame.mixer.music.get_busy() == True:
        continue
            
        #audio = generate(text=TEXT, voice=voice)
"""
    if not isinstance(audio, bytes):#from chat gpt, checks the type that is returned, and converts it to bytes it needed
        audio = b''.join(list(audio))
    play(audio)
    history = History.from_api()
    print(history)
"""
Speak("Hello what's up. I'm just hanging out.", 1)
