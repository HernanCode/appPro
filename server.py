""" import socket
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
            data = conn.recv(1026)  # Recibe un máximo de 1024 bytes
            statsList = data.decode('utf-8').split("ñ")
            ip = addr[0]
            print(ip)
            print(statsList) """

import os
def addServer(id, name, ip, oSystem, adminUser, adminPassword):
    path = "/etc/scripts/"    
    
    if oSystem == "Windows":
        path = ""


    os.system(f"ping {ip}")

addServer(1,1,"10.0.0.3",1,1,1);

