from django.urls import path
from . import views
from .views import ProcessTranscriptView, WebhookReceiver

app_name = "talkingcharacter"
urlpatterns = [
    path('view', views.CharacterView.as_view(), name="show_video"),
    path('process_transcript/', ProcessTranscriptView.as_view(), name='process_transcript'),
    path('get_server_status/', views.get_server_status, name='get_server_status'),
    path('webhook/', WebhookReceiver, name='webhook'),
    path('newest_video/', views.CharacterView.updateview, name='newest_link')
]