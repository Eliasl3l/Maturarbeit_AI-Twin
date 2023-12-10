
from django.urls import re_path
from talkingcharacter.consumers import MyConsumer
import os

#this would be for the websocket, but it isnt implemented so far
websocket_urlpatterns = [
    re_path(f'ws://{os.environ.get("NGROK_URL")}/ws/mywebsocket', MyConsumer.as_asgi()),
]