import os, subprocess
from pyngrok import ngrok
from django.conf import settings
from talkingcharacter import utils



# Setzen Sie hier Ihren Ngrok-Authentifizierungstoken ein
ngrok.set_auth_token("2XdB8236H2lY5VzmcI6CRhqgjcS_3phFKBeidpaa3TXMjhL5Y")

# Starten Sie den Ngrok-Prozess
public_url = ngrok.connect(8000)
host = public_url.public_url.split('//')[1].split(':')[0]
print(f"public url: {public_url}")
usable_url = public_url.public_url.split('"')[0]
print(usable_url)

# Setzen Sie die URL in Ihren Utils (falls erforderlich)
utils.ngrok_url = usable_url

os.environ['DJANGO_ALLOWED_HOSTS'] = host
django_server = subprocess.Popen(["python", "manage.py", "runserver"])

try:
    django_server.communicate()
except KeyboardInterrupt:
    django_server.terminate()
    ngrok.disconnect(public_url)
    ngrok.kill()




