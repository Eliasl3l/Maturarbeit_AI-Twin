from django.db import models
#from django.utils import timezone


"""
class Video(models.Model):
    caption=models.CharField(max_length=100, default='defaultCaption')
    pubdate=models.DateField(default=timezone.now)
    video=models.FileField(upload_to="video/%y", default='error')
    def __str__(self):
        return self.caption
"""
class ServerStatus(models.Model):
    status_text = models.CharField(max_length=255, default="Loading...")


class VideoLink(models.Model):
    video_link = models.URLField(max_length=200, default='https://8bf3-2a02-aa16-517b-2000-d867-6b56-c9af-30ae.ngrok-free.app/view')
    talk_id = models.CharField(max_length=60, default="")
    STATUS_CHOICES = [
        ('DONE', 'Erledigt'),
        ('PENDING', 'Ausstehend')
    ]
    status = models.CharField(max_length=7, choices=STATUS_CHOICES, default='PENDING')

    def __str__(self):
        return f"{self.video_link} - {self.status}"
