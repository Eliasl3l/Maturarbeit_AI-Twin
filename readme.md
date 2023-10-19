# Talking_Character (TC)
This program has the goal to make it possible to have a reallife conversation with a digital avatar. It achieves this goal using D-ID (a speaking avatar generator to a given text) and davinci-003 (a language processing tool by openai)
It is splitted into two versions, one that can run on any code editor, and one that can run on a localhost. (both require internet access)

## offline Version
sustains out of 4 different main functions
- text-to-speech
wich is basically speech recognition
- language processing 
which is basically like chatgpt
- text-to-video
which generates a video with an avatar speaking the given text
- main
which makes that all the four parts run smoothly one after another so you can have a real conversation with the avatar

## online Version
mainly sustains out of the classical django structure with the main function in the app Talking_Character
In this app the changed offline Version is in the utils file, and the speech recognition being in the the static folder, because it's in  css, so Client-based