import requests
from requests.auth import HTTPBasicAuth
import json
import time
#from makePresignedURL import create_presigned_url #for making PresignedURL which isn't necessary anymore, because the link isn't returned as s3 link anymore.
import os # for Videoplayer


USERNAME = 'ZWxpYXNsaW5kZW1hbm4wNUBnbWFpbC5jb20'
PASSWORD = 'SiNSSx9Bp22XWlrHHmx2X'
#TEXT = "Make sure the video file exists at the specified path before running this code. You can verify the path by navigating to the directory in File Explorer and checking for the file."


def make_video(TEXT, Num):    
    #make the video
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

    #inspired by chatGPT
    local_filename = f"Video{Num}.mp4"

    with requests.get(Video_id, stream=True) as r:
        r.raise_for_status()
        with open(local_filename, 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192):
                f.write(chunk)

    #copied from Chatgpt
    # Open the video with the default application for .mp4 files
    os.startfile(local_filename)

