import os
import queue
import requests
from requests.auth import HTTPBasicAuth
import json
import time
from . import secrets
import openai
from .models import VideoLink




NUM = 0
USERNAME = secrets.USERNAME_DID
PASSWORD = secrets.PASSWORD_DID
TOKEN_DID = secrets.TOKEN_DID
Newest_link = 'link.link@link.com'
ngrok_url=os.environ.get('NGROK_URL')
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

class video:
    videoID_URL = ""
    #this functions' code is mostly copied from https://docs.d-id.com/reference/overview  
    def request_video(TEXT, self):
        global Newest_link, ngrok_url, TOKEN_DID
        url = "https://api.d-id.com/talks"
        payload = {
            "script": {
                "type": "text",
                "input": TEXT  # Stellen Sie sicher, dass TEXT korrekt definiert ist
            },
            "source_url": "https://i.pinimg.com/564x/e7/d8/cd/e7d8cdfc7c14420aa6a46b9792806b83.jpg",
            "webhook": f"{ngrok_url}/webhook/"  # Stellen Sie sicher, dass ngrok_url korrekt definiert ist
        }

        headers = {
            "accept-encoding": "application/json",
            "content-type": "application/json",
            "Authorization": f"Basic {TOKEN_DID}"
        }

        response = requests.post(url, json.dumps(payload), headers=headers)
        
        print(response.text)
        
        #this part converts the json thing to a dictionary so i can load the id.
        response_string = response.text
        response_dict = json.loads(response_string)
        try:
            talk_id = response_dict['id']  # replace with your ID
        except KeyError:
            return TypeError

        return talk_id


    @staticmethod
    def get_video():
        print("getvideofuntion is now running")
        try:
            response = requests.get(video.videoID_URL, auth=HTTPBasicAuth( USERNAME, PASSWORD))
        except Exception as E:
            print(E)
            return E
        

        # If the video is returned in the response
        response_string2 = response.text
        response_dict2 = json.loads(response_string2)
        result_url = []
        result_url = response_dict2['result_url']
        print(result_url)
        return result_url
    
def create_video_db(talk_id):
    new_video = VideoLink.objects.create(video_link="default", video_id=talk_id, status='PENDING')

    return new_video.video_id

def update_video_link_and_set_done(talk_id, new_link):
    try:
        video = VideoLink.objects.get(video_id=talk_id)
        print(video.video_link)
        video.video_link = new_link
        video.status = 'DONE'
        video.save()
        print(new_link + " has been saved into the databank as new link")
        return video
    except VideoLink.DoesNotExist:
        print("Video mit der ID {} nicht gefunden.".format(talk_id))
        return None
"""
def test(Text):
    video.request_video(f"{Text}")
    time.sleep(5)
    video.get_video()
"""













"""
def make_video(TEXT):    
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
        "webhook": ADRESS
        
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
    try:
        talk_id = response_dict['id']  # replace with your ID
    except KeyError:
        return TypeError
    url = f"https://api.d-id.com/talks/{talk_id}"  # replace with the correct URL
    #for some reason the line above doesn't work, because it say internal server error, i think it is still the wrong url
    
    #needs to be replaced by webhook
    time.sleep(20)
    response = requests.get(url, auth=HTTPBasicAuth( USERNAME, PASSWORD))  # replace with your credentials
    #print(response.text) #this prints the fatass error message, its mostly facedetection error. Its because its the exact same prompt multiple times with the same text.
    # If the video is returned in the response
    response_string2 = response.text
    response_dict2 = json.loads(response_string2)
    #print(response_dict2)
    Video_id = []
    Video_id = response_dict2['result_url']
    print(Video_id)
    #Newest_link = Video_id
    return Video_id



def runface(transcript):
    response = get_chatgpt_response(transcript)
    print(f"Assistant: {response}")
    video_link = make_video(response)
    return video_link

"""
