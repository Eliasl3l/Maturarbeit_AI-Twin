"""
import pyttsx3
import tkinter as tk
import threading
import time
import requests

url = "https://api.elevenlabs.io/v1/models"

headers = {
  "Accept": "application/json",
  "xi-api-key": "67f3b63436afb1d0a558a87d22d05a40"
}

response = requests.get(url, headers=headers)

print(response.text)
# Initialize the text-to-speech engine
engine = pyttsx3.init()

# Define a simple "character" that can open and close its "mouth"
class Character:
    def __init__(self, canvas, x=50, y=50):
        self.mouth_open = False
        self.mouth = canvas.create_oval(x, y, x+100, y+100, outline='black', fill='black')

    def open_mouth(self, canvas):
        if not self.mouth_open:
            canvas.itemconfig(self.mouth, fill='red')
            self.mouth_open = True

    def close_mouth(self, canvas):
        if self.mouth_open:
            canvas.itemconfig(self.mouth, fill='black')
            self.mouth_open = False

def speak_and_animate(text, character, canvas):
    # This function will run in a separate thread
    for word in text.split():
        character.open_mouth(canvas)
        engine.say(word)
        engine.runAndWait()
        character.close_mouth(canvas)

# Create the tkinter window and canvas
root = tk.Tk()
canvas = tk.Canvas(root, width=200, height=200)
canvas.pack()

# Create the character
character = Character(canvas)

# The text the character will "say"
text = "Hello, I am a talking character."

# Start the speaking/animating in a separate thread so it doesn't block the tkinter event loop
threading.Thread(target=speak_and_animate, args=(text, character, canvas)).start()
root.mainloop()

import requests

CHUNK_SIZE = 1024
url = "https://api.elevenlabs.io/v1/text-to-speech/21m00Tcm4TlvDq8ikWAM"

headers = {
  "Accept": "audio/mpeg",
  "Content-Type": "application/json",
  "xi-api-key": "67f3b63436afb1d0a558a87d22d05a40"
}

data = {
  "text": "Hi! My name is Bella, nice to meet you!",
  "model_id": "eleven_monolingual_v1",
  "voice_settings": {
    "stability": 0.5,
    "similarity_boost": 0.5
  }
}

response = requests.post(url, json=data, headers=headers)
with open('output.mp3', 'wb') as f:
    for chunk in response.iter_content(chunk_size=CHUNK_SIZE):
        if chunk:
            f.write(chunk)
"""
#some copied code from the website
"""
import requests
USERNAME = eliaslindemann05@gmail.com
PASSWORD = saurier99

Authorization: Basic USERNAME:PASSWORD
ZWxpYXNsaW5kZW1hbm4wNUBnbWFpbC5jb20:NeW1BhLgVxtwnSWT1SdB3

{
    "source_url": "https://myhost.com/image.jpg",
    "script": {
        "type": "text",
        "input": "Hello world!"
    }
}
"""
#the basic authentification
import requests
from requests.auth import HTTPBasicAuth
import json
import time

USERNAME = 'ZWxpYXNsaW5kZW1hbm4wNUBnbWFpbC5jb20'
PASSWORD = 'SiNSSx9Bp22XWlrHHmx2X'
url = "https://api.d-id.com/animations"
headers = {
    "Content-Type": "application/json",
    "Accept": "application/json"
}
data = {
    "source_url": "https://public/path/to/image.jpg"
}

response = requests.post(url, headers=headers, data=data, auth=HTTPBasicAuth( USERNAME, PASSWORD))

print(response.status_code)

#make the video
url = "https://api.d-id.com/talks"
payload = {
    "script": {
        "type": "text",
        "input": "let this work pls.",
        "audio_url": "https://music.youtube.com/watch?v=VaNYrskkWBk",
        "provider": {
            "type": "microsoft",
            "voice_id": "en-US-JennyNeural"
        }
    },
    "face": {
        "top_left": [0, 0],
        "face_id": "1",
        "size": 512
    },
    "persist": True,
    "source_url": "https://create-images-results.d-id.com/google-oauth2%7C113737039728929273410/upl_zHRuunx8FrRkoXIJoxPCd/image.jpeg",
    "webhook": "https://host.domain.tld/to/webhook"
    #it always says facedetection error ,i dont know why.
}
headers = {
    "accept": "application/json",
    "content-type": "application/json"
}

response = requests.post(url, json=payload, headers=headers, auth=HTTPBasicAuth( USERNAME, PASSWORD))

print(response.text) 
#this part converts the json thing to a dictionary so i can load the id.
response_string = response.text
response_dict = json.loads(response_string)
talk_id = response_dict['id']  # replace with your ID
url = f"https://api.d-id.com/talks/{talk_id}"  # replace with the correct URL
#for some reason the line above doesn't work, because it say internal server error, i think it is still the wrong url
time.sleep(10)
response = requests.get(url, auth=HTTPBasicAuth( USERNAME, PASSWORD))  # replace with your credentials
print(response.text) #this prints the fatass error message, its mostly facedetection error. Its because its the exact same prompt multiple times with the same text.
# If the video is returned in the response
response_string2 = response.text
response_dict2 = json.loads(response_string)
Video_id = response_dict2['result_url']
print(Video_id)






#with open('video.mp4', 'wb') as f:
#    f.write(response.content)


