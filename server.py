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
        print(f"Conexión establecida desde {addr}")

        # Recibe los datos enviados por el cliente y los imprime en la consola
        ip = addr[0]
        with conn:
            print("Esperando datos del cliente...")
            data = conn.recv(1024)  # Recibe un máximo de 1024 bytes
            statsDict = pickle.loads(data)
            ip = addr[0]
            print(ip)
            print(statsDict)
    
            # Load the JSON data from file
            with open(f'data-{ip}.json', 'r') as f:
                file = json.load(f)

            # Add a number to the data array of cpuUsage dataset
            file["cpuUsage"]["data"].append(float(statsDict["cpuUsage"]))
            file["cpuUsage"]["data"].pop(0)
            file["memoryUsage"]["data"].append(float(statsDict["ramUsage"]))
            file["memoryUsage"]["data"].pop(0)
            file["serverUptime"]["current"] = statsDict["uptime"]
            file["storage"]["diskTotal"] = statsDict["diskTotal"]
            file["storage"]["diskUsed"] = statsDict["diskUsed"]

            # Save the modified JSON back to the file
            with open('data.json', 'w') as f:
                json.dump(file, f)


import os
def addServer(id, name, ip, oSystem, adminUser, adminPassword):
    path = "/home/prova/scripts"  
    command = f"sshpass -p {adminPassword} ssh-copy-id {adminUser}@{ip}"
    sendFile = f"scp localScript.py {adminUser}@{ip}:{path}"
    os.system(f'ssh {adminUser}@{ip} pip3 install psutil')
    os.system(f'ssh {adminUser}@{ip} pip3 install socket')
    if oSystem == "Windows": 
        path = ""

    os.system(command)
    os.system(f'ssh {adminUser}@{ip} "mkdir -p {path}"')
    os.system(f"{sendFile}client.py")
    
    os.system(f"echo '* * * * * {path}client.py' | ssh {adminUser}@{ip} 'cat >> ~/crontab && crontab ~/crontab'")
