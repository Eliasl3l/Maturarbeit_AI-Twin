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
"""
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

