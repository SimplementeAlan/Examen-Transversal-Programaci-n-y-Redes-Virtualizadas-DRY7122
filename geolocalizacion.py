import requests

api_key = '8811f4b0-8264-452b-a257-e50e627c153c'  # Reemplaza con tu clave API de Graphhopper

def obtener_ruta():
    while True:
        ciudad_origen = input("Ciudad de Origen ('s' para salir): ").strip()
        if ciudad_origen.lower() == 's':
            break
        
        ciudad_destino = input("Ciudad de Destino ('s' para salir): ").strip()
        if ciudad_destino.lower() == 's':
            break

        # Verificar si las ciudades están definidas en el diccionario
        ciudades = {
            'Santiago': '-33.4489,-70.6693',
            'Temuco': '-38.7359,-72.5904',
            'Valparaiso': '-33.0458,-71.6197'
        }

        punto_inicio = ciudades.get(ciudad_origen)
        punto_destino = ciudades.get(ciudad_destino)
        
        if not punto_inicio or not punto_destino:
            print(f"Coordenadas no encontradas para {ciudad_origen} o {ciudad_destino}.")
            continue

        # URL de la solicitud
        url = f'https://graphhopper.com/api/1/route?point={punto_inicio}&point={punto_destino}&vehicle=car&locale=es&key={api_key}'
        
        # Realiza la solicitud
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            if 'paths' in data:
                path = data['paths'][0]
                distancia = path['distance'] / 1000  # Convertir a kilómetros
                tiempo = path['time'] / 1000 / 60  # Convertir a minutos
                print(f"Distancia: {distancia:.2f} km")
                print(f"Tiempo estimado: {tiempo:.2f} minutos")
                print("Narrativa del viaje:")
                for instruccion in path['instructions']:
                    print(f"{instruccion['text']} (por {instruccion['distance']} metros)")
            else:
                print("No se encontró la ruta.")
        else:
            print(f"Error en la solicitud: {response.status_code}")

# Ejecutar la función para obtener la ruta
obtener_ruta()



