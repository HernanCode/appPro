import socket
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
        with conn:
            print("Esperando datos del cliente...")
            data = conn.recv(1024)  # Recibe un máximo de 1024 bytes
            statsList = data.decode('utf-8').split("ñ")
            ip = addr[0]
            print(ip)
            print(statsList)


import os
def addServer(id, name, ip, oSystem, adminUser, adminPassword):

    os.system(f'ssh {adminUser}@{ip} pip3 install psutil')
    os.system(f'ssh {adminUser}@{ip} pip3 install socket')

    path = "/home/prova/scripts"    

    command = f"sshpass -p {adminPassword} ssh-copy-id {adminUser}@{ip}"
    sendFile = f"scp localScript.py {adminUser}@{ip}:{path}"

    if oSystem == "Windows": 
        path = ""

    os.system(command)
    os.system(f'ssh {adminUser}@{ip} "mkdir -p {path}"')
    os.system(f"{sendFile}script1")
    
    os.system(f"echo '* * * * * {path}script1' | ssh {adminUser}@{ip} 'cat >> ~/crontab && crontab ~/crontab'")


#modify json
import json

# Load the JSON file
with open('data.json', 'r') as f:
    data = json.load(f)

# Modify the "storage" data
data["storage"]["data"][0]["value"] = 750

# Save the modified JSON back to the file
with open('data.json', 'w') as f:
    json.dump(data, f)
