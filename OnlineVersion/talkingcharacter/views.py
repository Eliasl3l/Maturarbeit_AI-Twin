
from django.views.generic import TemplateView
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from .models import ServerStatus
from django.utils.decorators import method_decorator
from django.views import View
import json
from .utils import video, Newest_link


status_text = "standard"


#def startconversation(request)
@method_decorator(csrf_exempt, name='dispatch')
class ProcessTranscriptView(View):

    #I still have to check if D-ID acutally sends a post- and not a get request 
    def post(self, request):
        global status_text, Newest_link, new_status, transcript
        data = json.loads(request.body)
        transcript = data.get('transcript', '')
        
        try:
            x = video.request_video(transcript, self)   
        except Exception as E:
            print(E + "video.requestvideo didnt work")
            return JsonResponse({"something with the video request went wrong"})
        status_text = "The video has actually been processed"
        print("the video has actually been processed")

        new_status = "The video has actually been processed"

        # For demonstration purposes, we'll just echo it back
        
        return JsonResponse({"message": "Audio received successfully!"})

class CharacterView(TemplateView):
    template_name = "index.html"
    def updateview(link, request):
        #funtion that ONLY updates the video
        context = {'video_link': Newest_link}
        return render(request, "index.html", context)
        






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
        link = video.get_video(request)
        CharacterView.updateview(link)
        return JsonResponse({'status':'webhook worked'}, safe=False)
    
    def get(self, request):
        link = video.get_video(request)
        CharacterView.updateview(link)
        return JsonResponse({'status':'webhook worked'}, safe=False)
    



    