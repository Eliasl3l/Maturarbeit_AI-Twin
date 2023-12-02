
from django.urls import re_path
from talkingcharacter.consumers import MyConsumer
import os

websocket_urlpatterns = [
    re_path(f'ws://{os.environ.get("NGROK_URL")}/ws/mywebsocket', MyConsumer.as_asgi()),
]