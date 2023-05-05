import socket, json, pickle 

HOST = ''  
PORT = 12345 
#Starts to listen to the port we defined
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
    server.bind((HOST, PORT))
    server.listen()

    while True:
        #When receiveng a connection, stores the address (ip, port) and the data received
        conn, addr = server.accept()
        print(f"Connection established with {addr}")

        ip = addr[0]

        with conn:
            #Sets the maximum amount of data that can be received to 1024 bytes
            data = conn.recv(1024) 
            #Deserializes the data to a dictionary 
            statsDict = pickle.loads(data)
            ip = addr[0]

            #Opens and writes the data to the corresponding .json file
            with open(f'/home/samuel/appPro/myPanel/static/json/json-{ip}.json', 'r') as f:
                file = json.load(f)

            file["cpuUsage"]["data"].append(float(statsDict["cpuUsage"]))
            file["cpuUsage"]["data"].pop(0)
            file["memoryUsage"]["data"].append(float(statsDict["ramUsage"]))
            file["memoryUsage"]["data"].pop(0)
            file["storage"]["diskTotal"] = statsDict["diskTotal"]
            file["storage"]["diskUsed"] = statsDict["diskUsed"]

            with open(f'/home/samuel/appPro/myPanel/static/json/json-{ip}.json', 'w') as f:
                json.dump(file, f)

