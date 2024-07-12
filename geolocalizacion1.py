import requests

api_key = "8811f4b0-8264-452b-a257-e50e627c153c"
url = "https://graphhopper.com/api/1/route"

while True:
    origen = input("Ciudad de Origen: ")
    destino = input("Ciudad de Destino: ")

    if origen.lower() == 's' or destino.lower() == 's':
        break

    params = {
        'point': [origen, destino],
        'vehicle': 'car',
        'locale': 'es',
        'instructions': 'true',
        'calc_points': 'true',
        'key': api_key
    }

    response = requests.get(url, params=params)
    data = response.json()

    if 'paths' in data:
        path = data['paths'][0]
        distancia_km = path['distance'] / 1000
        duracion_seg = path['time'] / 1000
        distancia_millas = distancia_km * 0.621371

        horas = int(duracion_seg // 3600)
        minutos = int((duracion_seg % 3600) // 60)

        print(f"Distancia: {distancia_km:.2f} km ({distancia_millas:.2f} millas)")
        print(f"Duración: {horas} horas y {minutos} minutos")
        print("Narrativa del viaje:")
        for instruccion in path['instructions']:
            print(f"{instruccion['text']} (por {instruccion['distance']} metros)")

        medio_transporte = input("Tipo de medio de transporte: ")
    else:
        print("No se pudo calcular la ruta. Por favor, intente nuevamente.")

