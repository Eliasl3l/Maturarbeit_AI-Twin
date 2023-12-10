import json
from channels.generic.websocket import AsyncWebsocketConsumer

#this would be for the websocket, which isn't implemented so far
class MyConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()

    async def disconnect(self, close_code):
        pass

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            'message': message
        }))
    
    async def send_video_url(self, video_url):
        await self.send(text_data=json.dumps({
            'video_url': video_url
        }))