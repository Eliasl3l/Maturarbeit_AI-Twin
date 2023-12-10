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
#uses the OPENAI API to get a text response to the given prompt from the model ChatGPT 3.5 Turbo 
def get_chatgpt_response(query):
    chat_completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "user",
                "content": query,
            }
        ]
    )


    return chat_completion['choices'][0]['message']['content']
# this class is responsible for requesting of the video from the D-ID Server
class video:
    videoID_URL = ""
    #this functions' code is mostly copied from https://docs.d-id.com/reference/overview  
    def request_video(TEXT, self):
        global Newest_link, ngrok_url, TOKEN_DID
        url = "https://api.d-id.com/talks"
        payload = {
            "script": {
                "type": "text",
                "input": TEXT,  
                "provider":{
                    "type":"elevenlabs",
                    "voice_id":"CYw3kZ02Hs0563khs1Fj"
                }
            },
            "source_url": "https://create-images-results.d-id.com/google-oauth2%7C113737039728929273410/upl_Q5dA_a3eLK93IE1GLtNCQ/image.jpeg",
            "webhook": f"{ngrok_url}/webhook/" 
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

    #this function gets the video from the D-Id server, but it isn't in use anymore
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
    #this first creates an instance in the database with the video id, where the video URL is added later
def create_video_db(talk_id):
    new_video = VideoLink.objects.create(video_link="default", video_id=talk_id, status='PENDING')

    return new_video.video_id
# this function adds the Video URL to the database instance with the according ID
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


