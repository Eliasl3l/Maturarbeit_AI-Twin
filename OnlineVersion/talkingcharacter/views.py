
from django.views.generic import TemplateView
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from .models import ServerStatus
from django.utils.decorators import method_decorator
from django.views import View
import json
from .utils import main1, Newest_link
from django.http import JsonResponse
import queue

status_text = "standard"
audio_queue = queue.Queue()

def receive_audio(request):
    if request.method == 'POST':
        audio_file = request.FILES.get('audio_file')

        if audio_file:
            # Do something with the audio file
            # For example, put it in a shared queue (which you'll need to define elsewhere)
            audio_queue.put(audio_file)

        return JsonResponse({"message": "Audio received successfully!"})
    return JsonResponse({"message": "Invalid method or missing file."})

@method_decorator(csrf_exempt, name='dispatch')
class ProcessTranscriptView(View):

    def post(self, request, *args, **kwargs):
        data = json.loads(request.body)
        transcript = data.get('transcript', '')

        # Process the transcript as needed
        # For demonstration purposes, we'll just echo it back
        return JsonResponse({"received_transcript": transcript})

class CharacterView(TemplateView):
    template_name = "index.html"

    def show_video(self,**kwargs):
        global Newest_link
        while True:
            if not audio_queue.empty():
                audio_file = audio_queue.get()
                print("main is running")
                main1(audio_file)
                context = {'video_link': Newest_link}
                return render(self.request, 'index.html', context) 
            # Process the audio file here, e.g., transcribe, analyze, etc.

from django.http import JsonResponse

def get_server_status(request):
    # Your logic to determine server status. For demonstration:
    global status_text

    return JsonResponse({"status": status_text})


@require_POST
def update_server_status(request):
    new_status = request.POST.get('status_text')
    if new_status:
        ServerStatus.objects.create(status_text=new_status)
        return JsonResponse({"message": "Status updated successfully!"})
    else:
        return JsonResponse({"error": "Status text not provided!"}, status=400)
    



    