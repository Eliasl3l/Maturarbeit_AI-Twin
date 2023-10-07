
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
import time
#import subprocess


status_text = "standard"


def receive_audio(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        # Get the 'transcript' value from the JSON data
        transcript = data.get('transcript')
        #audio_file = request.FILES.get('audio_file')
        if transcript:
            global status_text, new_status, Newest_link
            
            
            # Do something with the audio file
            # For example, put it in a shared queue (which you'll need to define elsewhere)
            
            Newest_link = runface(transcript)
            
            status_text = f"This is the newest link {Newest_link}"

            context = {'video_link': Newest_link}
            render(request, 'index.html', context)
            status_text = f"it should have been processed"
        
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
            #result = subprocess.run([runface, transcript], text=True, capture_output=True)
            #Newest_link = result.stdout
            new_status = f"The video has actually been processed"
            #while True:
             #   if Newest_link:
              #      break
            
        # Process the transcript as needed
        # For demonstration purposes, we'll just echo it back
            
            return JsonResponse({"video_link": Newest_link})

class CharacterView(TemplateView):
    template_name = "index.html"
    def updateview(link, request):
        #funtion that ONLY updates the video
        context = {'video_link': Newest_link}
        return render(request, 'index.html', context)
        






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
 
    
@method_decorator(csrf_exempt, name='dispatch')
class WebhookView(View):

    def post(self, request):
        payload = request.body
        print(payload)
        return JsonResponse({'status':'webhook worked'}, safe=False)
    



    