import requests
from requests.auth import HTTPBasicAuth
import json # Importiert das json-Modul zum Parsen von JSON-Daten
import time # Importiert das time-Modul für Zeit-basierte Funktionen wie sleep
#from makePresignedURL import create_presigned_url #for making PresignedURL which isn't necessary anymore, because the link isn't returned as s3 link anymore.
import os # for Videoplayer

# Anmeldedaten für die API
USERNAME = 'ZWxpYXNsaW5kZW1hbm4wNUBnbWFpbC5jb20'
PASSWORD = 'N0tBFK-JUJhP25z7NqrYL'

#the code for the communication with the server ist mostly from https://docs.d-id.com/reference/overview 

def make_video(TEXT, Num):    
    # Funktion, um ein Video basierend auf gegebenem Text zu erstellen
    # Definiert die URL und die Payload (Daten) für die POST-Anfrage an die API
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
        #"persist": True, # optional, um das Video dauerhaft zu speichern
        "source_url": "https://i.pinimg.com/564x/e7/d8/cd/e7d8cdfc7c14420aa6a46b9792806b83.jpg",
        "webhook": "https://host.domain.tld/to/webhook"
        #it always says facedetection error ,i dont know why.
    }
    headers = {
        "accept": "application/json",
        "content-type": "application/json"
    }

    # Sendet die POST-Anfrage mit den definierten Daten und Anmeldedaten
    response = requests.post(url, json=payload, headers=headers, auth=HTTPBasicAuth( USERNAME, PASSWORD))

    print(response.text) # Zeigt die Antwort der API im Textformat an
    
    # Konvertiert die JSON-Antwort in ein Python-Wörterbuch
    response_string = response.text
    response_dict = json.loads(response_string)
    talk_id = response_dict['id'] 
    url = f"https://api.d-id.com/talks/{talk_id}"  # Fügt den Anfang der URL und die ID zusammen 
    #for some reason the line above doesn't work, because it say internal server error, i think it is still the wrong url
    
    # Wartet 10 Sekunden, um der API Zeit zu geben, das Video zu verarbeiten
    time.sleep(10)
    # Ruft das erstellte Video von der API ab
    response = requests.get(url, auth=HTTPBasicAuth( USERNAME, PASSWORD))  # replace with your credentials
    
    # Extrahiert die URL des Videos aus der Antwort
    response_string2 = response.text
    response_dict2 = json.loads(response_string2)
    #print(response_dict2)
    Video_id = []
    Video_id = response_dict2['result_url']
    print(Video_id)

    #mostly written by chatGPT 3.5
    local_filename = f"Video{Num}.mp4" # Der lokale Dateiname für das Video

    # Lädt das Video von der angegebenen URL herunter und speichert es lokal
    with requests.get(Video_id, stream=True) as r:
        r.raise_for_status()
        with open(local_filename, 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192):
                f.write(chunk)

    
    # Öffnet das Video mit der Standardanwendung für .mp4-Dateien
    os.startfile(local_filename)

