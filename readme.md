# AI Twin: talk to your own AI twin
This program has the goal to make it possible to have a reallife conversation with a digital avatar. It achieves this goal using D-ID (a speaking avatar generator to a given text) and davinci-003/ChatGPT 3.5 Turbo (a language processing tool by openai)
It is splitted into two versions, one that can run on any code editor, and one that can run on a ngrok tunnel. (both require internet access)

## offline Version
sustains out of 4 different main files
- text-to-speech
wich is basically speech recognition
- language processing 
which is basically like chatgpt
- text-to-video
which generates a video with an avatar speaking the given text
- main
which makes that all the four parts run smoothly one after another so you can have a real conversation with the avatar

![Maturpräsentation offline Version](https://github.com/Eliasl3l/Maturarbeit_AI-Twin/assets/59790316/74ed3e63-6290-4f72-bd9d-9c227cff0919)
This is a visual representation of the state machine. (German)

## online Version
mainly sustains out of the classical django structure with the main function in the app Talking_Character
In this Version the functionality of the offline Version is moved into the utils.py file, except for speech recognition which is done in the frontend and part where the video url is requested from the D-ID Server, because it is now sent through a webhook. The client makes Post requests to the webapp until the video url is saved in the database and is sent to the client as a JsonResponse. Then the client plays the video.

![Maturpräsentation Ausführung Webapp OnlyGreen](https://github.com/Eliasl3l/Maturarbeit_AI-Twin/assets/59790316/ba13cbb7-acc3-4a7d-bf59-e9d711884218)
This is a visual representation of the datatraffic on the webapp after a videorequest has been made from the client. The colors of the arrows can be ignored.

Important: you can only run this localhost server if you have an OpenAI API acoount (paid), a D-ID subscription (paid), an NGROK account (free) and a Cloudinary account (free). Additionally you need to run migrations before starting the server. (py manage.py makemigrations) (py manage.py migrate)
