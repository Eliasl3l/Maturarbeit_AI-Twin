from django.test import TestCase
from . import secrets, utils
import openai
import cv2
import urllib.request


class Secretkeytesting(TestCase):
    def test_openaikey_isStillWorking(self):
        openai.api_key = secrets.OPENAI_KEY
        try:
            response = openai.Completion.create(
                engine="davinci",
                prompt="say 'Hello' in German",
                max_tokens=5
            )
        except Exception as E:
            self.fail(E)
        else:
            responseText = response.choices[0].text.strip()
            print(responseText)
            self = True
    
    def test_videoAnimation(self):
        try:
            responseVideo = utils.make_video("hello")
        except Exception as E:
            self.fail(E)
        else:
            url = responseVideo
            urllib.request.urlretrieve(url, "video.mp4")

            cap = cv2.VideoCapture("video.mp4")

            while cap.isOpened():
                ret, frame = cap.read()
                if not ret:
                    break  # Exit loop at end of video
                cv2.imshow('Video', frame)
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break  # Exit loop on 'q' key press

            cap.release()
            cv2.destroyAllWindows()
            self = True

# The video Test doesn't work yet because of an errror of the cv2 module
        
class UtilsTesting(TestCase):
    def GPTResponseTest(self):
        try:
            responseText = utils.get_chatgpt_response("say 'Hello' in German")
        except Exception as E:
            self.fail(E)
        else: 
            print(responseText)
            self = True
    
    
