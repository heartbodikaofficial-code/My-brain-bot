import os
import time
import datetime
import requests
from twilio.rest import Client

# Configuration via Variables d'Environnement (Sécurité !)
TWILIO_SID = os.environ.get('TWILIO_SID')
TWILIO_TOKEN = os.environ.get('TWILIO_TOKEN')
NUMERO_DEST = '+243977223393'
NUMERO_SANDBOX = '+14155238886'

client = Client(TWILIO_SID, TWILIO_TOKEN)

def envoyer_meteo():
    # 1. Récupérer la météo
    url = "https://api.open-meteo.com/v1/forecast?latitude=-11.66&longitude=27.48&current_weather=true"
    donnees = requests.get(url).json()
    temp = donnees['current_weather']['temperature']
    
    # 2. Préparer le message
    message = f"☀️ Bonjour Heart Bodika !\n\nIl est 07:00 à Lubumbashi.\nLa température actuelle est de {temp}°C.\n\nPasse une excellente journée ! 🧠"
    
    # 3. Envoyer
    client.messages.create(
        from_=f"whatsapp:{NUMERO_SANDBOX}",
        body=message,
        to=f"whatsapp:{NUMERO_DEST}"
    )
    print("Météo envoyée !")

# Boucle infinie pour le serveur
print("Le Bot My Brain 🧠 est en ligne et attend 07:00...")
while True:
    maintenant = datetime.datetime.now()
    
    # Vérifie s'il est 07:00 (Heure du serveur, souvent UTC)
    if maintenant.hour == 5 and maintenant.minute == 0: # 05:00 UTC = 07:00 Lubumbashi
        envoyer_meteo()
        time.sleep(60) # Attend 1 min pour ne pas renvoyer le message
    
    time.sleep(30) # Vérifie toutes les 30 secondes
