
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
from django.http import JsonResponse
import queue
from .utils import audio_queue

status_text = "standard"


def receive_audio(request):
    if request.method == 'POST':
        audio_file = request.FILES.get('audio_file')
        render(request, 'testtemplate.html')
        if audio_file:
            global status_text, new_status
            # Do something with the audio file
            # For example, put it in a shared queue (which you'll need to define elsewhere)
            audio_queue.put(audio_file)
            new_status = f"The video will actually be processed"
            runface(audio_queue.get())
            
            status_text = f"This is the newest link {Newest_link}"
            #context = {'video_link': Newest_link}
            #render(request, 'index.html', context)
            status_text = f"it should have been processed"
            

        return JsonResponse({"message": "Audio received successfully!"})
    return JsonResponse({"message": "Invalid method or missing file."})

#def startconversation(request)
@method_decorator(csrf_exempt, name='dispatch')
class ProcessTranscriptView(View):

    def post(self, request, *args, **kwargs):
        global status_text, Newest_link, new_status
        data = json.loads(request.body)
        transcript = data.get('transcript', '')
        status_text = f"This is the newest link {Newest_link}"
        runface(audio_queue.get)
        new_status = f"The video has actually been processed"
        context = {'video_link': Newest_link}
        
        # Process the transcript as needed
        # For demonstration purposes, we'll just echo it back
        return render(request, 'index.html', context)
#JsonResponse({"received_transcript": transcript})
class CharacterView(TemplateView):
    template_name = "index.html"


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
    



    