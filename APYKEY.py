api_key = '8811f4b0-8264-452b-a257-e50e627c153c'

import requests

# Reemplaza con tu clave API
api_key = '8811f4b0-8264-452b-a257-e50e627c153c'

# Puntos de inicio y destino
punto_inicio = '52.517037,13.38886'  # Berlín
punto_destino = '52.529407,13.397634'  # Berlín

# URL de la solicitud
url = f'https://graphhopper.com/api/1/route?point={punto_inicio}&point={punto_destino}&vehicle=car&locale=de&key={api_key}'

# Realiza la solicitud
response = requests.get(url)
data = response.json()

# Imprime la respuesta
print(data)
