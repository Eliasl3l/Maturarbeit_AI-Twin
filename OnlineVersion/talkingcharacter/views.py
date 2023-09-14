
from django.views.generic import TemplateView
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from .models import ServerStatus
from django.utils.decorators import method_decorator
from django.views import View
import json
from .utils import runface, Newest_link
import queue
from .utils import audio_queue


status_text = "standard"


def receive_audio(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        # Get the 'transcript' value from the JSON data
        transcript = data.get('transcript')
        #audio_file = request.FILES.get('audio_file')
        render(request, 'testtemplate.html')
        if transcript:
            global status_text, new_status
            """
            
            # Do something with the audio file
            # For example, put it in a shared queue (which you'll need to define elsewhere)
            audio_queue.put(transcript)
            new_status = f"The video will actually be processed"
            s = audio_queue.get()
            runface(s)
            
            status_text = f"This is the newest link {Newest_link}"

            #context = {'video_link': Newest_link}
            #render(request, 'index.html', context)
            status_text = f"it should have been processed"
            """
            status_text = "the audio has been received"

        return JsonResponse({"message": "Audio received successfully!"})
    return JsonResponse({"message": "Invalid method or missing file."})

#def startconversation(request)
@method_decorator(csrf_exempt, name='dispatch')
class ProcessTranscriptView(View):

    def post(self, request):
        if request.method == 'POST':
            global status_text, Newest_link, new_status, transcript
            data = json.loads(request.body)
            transcript = data.get('transcript', '')
            #s = audio_queue.get()
            Newest_link = runface(transcript)
            new_status = f"The video has actually been processed"
            
        
        # Process the transcript as needed
        # For demonstration purposes, we'll just echo it back
        return JsonResponse({"video_link": Newest_link})
class CharacterView(TemplateView):
    template_name = "index.html"




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
    



    