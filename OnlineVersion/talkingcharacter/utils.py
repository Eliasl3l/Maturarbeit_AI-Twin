import os
import queue
import requests
from requests.auth import HTTPBasicAuth
import json
from . import secrets
from openai import OpenAI
from .models import VideoLink
import cloudinary, cloudinary.uploader, cloudinary.api


NUM = 0
USERNAME = secrets.USERNAME_DID
PASSWORD = secrets.PASSWORD_DID
TOKEN_DID = secrets.TOKEN_DID
Newest_link = 'link.link@link.com'
ngrok_url=os.environ.get('NGROK_URL')
# Shared audio queue for the entire application
audio_queue = queue.Queue()
# Presumably, other supporting functions will be here like get_chatgpt_response and make_video



#uses the OPENAI API to get a text response to the given prompt from the model ChatGPT 3.5 Turbo
client = OpenAI(
    # This is the default and can be omitted
    api_key= secrets.OPENAI_KEY,
)
def get_chatgpt_response(prompt):
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": prompt,
            }
        ],
        model="gpt-3.5-turbo",
        max_tokens=100
    )
    content = chat_completion.choices[0].message.content

    return content





# this class is responsible for requesting of the video from the D-ID Server
class video:
    videoID_URL = ""
    #this functions' code is mostly copied from https://docs.d-id.com/reference/overview  
    def request_video(TEXT, self, image_url):
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
            "source_url": image_url,
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
            talk_id = response_dict['id'] 
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




def uploadImage(image):
    cloudinary.config( 
    cloud_name = secrets.SDK_CLOUD_NAME, 
    api_key = secrets.SDK_API_KEY, 
    api_secret = secrets.SDK_API_SECRET 
    )

    # Set configuration parameter: return "https" URLs by setting secure=True  
    config = cloudinary.config(secure=True)


    print("Credentials: ", config.cloud_name, config.api_key)

    #need to change that urgently, is a big mess if all the images have same id !!!!!!
    # Upload the image and get its URL
    public_id = "sheeshkebab123"
    # Upload the image.
    response = cloudinary.uploader.upload(image, use_filename = True, public_id = public_id)

    srcURL = response['secure_url']
    # Log the image URL to the console. 
    print("Delivery URL: ", srcURL)
    return srcURL