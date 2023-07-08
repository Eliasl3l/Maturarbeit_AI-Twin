from elevenlabs import clone, generate, play, set_api_key
from elevenlabs.api import History
#https://docs.elevenlabs.io/api-reference/quick-start/introduction  for Documentation
#https://github.com/elevenlabs/elevenlabs-python/tree/main  Github Page
set_api_key("67f3b63436afb1d0a558a87d22d05a40")

voice = clone(
    name="Voice Name",
    description="An old American male voice with a slight hoarseness in his throat. Perfect for news.",
    files=["./sample1.mp3", "./sample2.mp3"],
)

audio = generate(text="Some very long text to be read by the voice", voice=voice)

play(audio)

history = History.from_api()
print(history)
  
