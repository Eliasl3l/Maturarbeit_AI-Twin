import os
import queue
#from .TextToVideo import make_video
import requests
from requests.auth import HTTPBasicAuth
import json
import time
from . import secrets
import openai


# Assuming other required imports are added as needed
NUM = 0
USERNAME = secrets.USERNAME_DID
PASSWORD = secrets.PASSWORD_DID
Newest_link = ''
# Shared audio queue for the entire application
audio_queue = queue.Queue()
# Presumably, other supporting functions will be here like get_chatgpt_response and make_video




openai.api_key = secrets.OPENAI_KEY
language = 'en'

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

def make_video(TEXT, Num):    
    #make the video
    global Newest_link
    url = "https://api.d-id.com/talks"
    payload = {
        "script": {
            "type": "text",
            "input": TEXT,
            "provider": {
                "type": "microsoft",
                "voice_id": "en-US-JennyNeural"
            }
        },
        "face": {
            "top_left": [5, -5],
            "face_id": "1",
            "size": 512
        },
        #"persist": True,
        "source_url": "https://i.pinimg.com/564x/e7/d8/cd/e7d8cdfc7c14420aa6a46b9792806b83.jpg",
        "webhook": "https://host.domain.tld/to/webhook"
        #it always says facedetection error ,i dont know why.
        #still have to integrate an actual webhook
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
    #print(response.text) #this prints the fatass error message, its mostly facedetection error. Its because its the exact same prompt multiple times with the same text.
    # If the video is returned in the response
    response_string2 = response.text
    response_dict2 = json.loads(response_string2)
    #print(response_dict2)
    Video_id = []
    Video_id = response_dict2['result_url']
    print(Video_id)
    Newest_link = Video_id




def main1(audio_file):
    global NUM
    response = get_chatgpt_response(audio_file)
    print(f"Assistant: {response}")
    make_video(response, NUM) 

def main1():
    global NUM
    global Newest_link
    while True:
        if not audio_queue.empty():
            audio_file = audio_queue.get()
            response = get_chatgpt_response(audio_file)
            print(f"Assistant: {response}")
            make_video(response, NUM)
   




