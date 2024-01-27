import os, subprocess, django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'main.settings')
django.setup()

from pyngrok import ngrok
from django.conf import settings
from talkingcharacter.utils import ngrok_url
from talkingcharacter import secrets


# inspired by https://ngrok.com/docs/
# Setzen Sie hier Ihren Ngrok-Authentifizierungstoken ein
ngrok.set_auth_token(secrets.NGROK_AUTH_TOKEN)

# Starten Sie den Ngrok-Prozess
public_url = ngrok.connect(8000)
host = public_url.public_url.split('//')[1].split(':')[0]
print(f"public url: {public_url}")
usable_url = public_url.public_url.split('"')[0]
os.environ['NGROK_URL'] = usable_url
print(f"{usable_url}/view")

# Setzen Sie die URL in Ihren Utils (falls erforderlich)
ngrok_url = usable_url

os.environ['DJANGO_ALLOWED_HOSTS'] = host
django_server = subprocess.Popen(["python", "manage.py", "runserver"])

try:
    django_server.communicate()
except KeyboardInterrupt:
    django_server.terminate()
    ngrok.disconnect(public_url)
    ngrok.kill()




