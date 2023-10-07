import os, subprocess
from pyngrok import ngrok
from django.conf import settings



# Start ngrok tunnel
public_url = ngrok.connect(8000)
host = public_url.public_url.split('//')[1].split(':')[0]
print(f"public url: {public_url}")


os.environ['DJANGO_ALLOWED_HOSTS'] = host
django_server = subprocess.Popen(["python", "manage.py", "runserver"])

try:
    django_server.communicate()
except KeyboardInterrupt:
    django_server.terminate()
    ngrok.disconnect(public_url)
    ngrok.kill()