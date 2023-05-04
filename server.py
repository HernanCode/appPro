import socket
import json
import pickle 

HOST = ''  # Indica que se aceptarán conexiones de cualquier dirección IP
PORT = 12345  # Puerto en el que el servidor escuchará las conexiones

# Crea un socket y lo vincula al host y puerto especificados
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as servidor:
    servidor.bind((HOST, PORT))
    servidor.listen()

    print(f"Servidor escuchando en el puerto {PORT}...")

    # Acepta una nueva conexión y obtiene el socket y la dirección del cliente
    while True:
        conn, addr = servidor.accept()
        print(f"Connection established with {addr}")

        # Recibe los datos enviados por el cliente y los imprime en la consola
        ip = addr[0]
        with conn:
            data = conn.recv(1024)  # Recibe un máximo de 1024 bytes
            statsDict = pickle.loads(data)
            ip = addr[0]
    
            # Load the JSON data from file
            with open(f'/home/samuel/appPro/myPanel/static/json/json-{ip}.json', 'r') as f:
                file = json.load(f)

            # Add a number to the data array of cpuUsage dataset
            file["cpuUsage"]["data"].append(float(statsDict["cpuUsage"]))
            file["cpuUsage"]["data"].pop(0)
            file["memoryUsage"]["data"].append(float(statsDict["ramUsage"]))
            file["memoryUsage"]["data"].pop(0)
            file["storage"]["diskTotal"] = statsDict["diskTotal"]
            file["storage"]["diskUsed"] = statsDict["diskUsed"]

            # Save the modified JSON back to the file
            with open(f'/home/samuel/appPro/myPanel/static/json/json-{ip}.json', 'w') as f:
                json.dump(file, f)

