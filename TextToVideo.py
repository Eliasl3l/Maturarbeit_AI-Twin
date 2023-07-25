import requests
from requests.auth import HTTPBasicAuth
import json
import time

USERNAME = 'ZWxpYXNsaW5kZW1hbm4wNUBnbWFpbC5jb20'
PASSWORD = 'SiNSSx9Bp22XWlrHHmx2X'
TEXT = "bla bla bla"
"""
url = "https://api.d-id.com/animations"
headers = {
    "Content-Type": "application/json",
    "Accept": "application/json"
}
data = {
    "source_url": "https://create-images-results.d-id.com/google-oauth2%7C113737039728929273410/upl_zHRuunx8FrRkoXIJoxPCd/image.jpeg"
}

response = requests.post(url, headers=headers, data=data, auth=HTTPBasicAuth( USERNAME, PASSWORD))

print(response.status_code)
"""
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
    "persist": True,
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
print(response.text) #this prints the fatass error message, its mostly facedetection error. Its because its the exact same prompt multiple times with the same text.
# If the video is returned in the response
response_string2 = response.text
response_dict2 = json.loads(response_string2)
print(response_dict2)
#Video_id = response_dict2['result_url']
#print(Video_id)