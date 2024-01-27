from django.db import models
#from django.utils import timezone



class ServerStatus(models.Model):
    status_text = models.CharField(max_length=255, default="Loading...")

# in this class the Video ID and the Video URL is saved from each produced video
class VideoLink(models.Model):
    video_link = models.URLField(max_length=200, default='https://8bf3-2a02-aa16-517b-2000-d867-6b56-c9af-30ae.ngrok-free.app/view')
    video_id = models.CharField(max_length=60, default="")
    STATUS_CHOICES = [
        ('DONE', 'Erledigt'),
        ('PENDING', 'Ausstehend')
    ]
    status = models.CharField(max_length=7, choices=STATUS_CHOICES, default='PENDING')

    def __str__(self):
        return f"{self.video_link} - {self.status}"

class MyModel(models.Model):
    image = models.ImageField(upload_to='images/')
