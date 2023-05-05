import socket, psutil, time, pickle

#Script that will be sent to the client

#Returns some stats of the client
def getStats():    
    cpuUsage = psutil.cpu_percent(5)
    ramUsage = round(psutil.virtual_memory().percent)
    diskUsage = psutil.disk_usage('/')
    uptime = time.time() - psutil.boot_time()
    data = {
        "cpuUsage":cpuUsage,
        "ramUsage":ramUsage,
        "diskTotal":round(diskUsage.total/1000000000,1),
        "diskUsed":round(diskUsage.used/1000000000,1), 
        "uptime":uptime}
    return pickle.dumps(data)

#Sends the stats to the server
def sendStats(host,port,stats):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
        client.connect((host,port))
        client.sendall(stats)
        print("Datos enviados al servidor.")

host = '10.0.0.1'
port = 12345

sendStats(host,port,getStats())



