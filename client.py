import socket
import psutil
import time
import pickle

def getStats():    
    cpuUsage = psutil.cpu_percent(50)
    ramUsage = round(psutil.virtual_memory().used/1000000000,1)
    diskUsage = psutil.disk_usage('/')
    print(ramUsage)
    print(diskUsage)
    uptime = time.time() - psutil.boot_time()
    data = {
        "cpuUsage":cpuUsage,
        "ramUsage":ramUsage,
        "diskTotal":round(diskUsage.total/1000000000,1),
        "diskUsed":round(diskUsage.used/1000000000,1), 
        "uptime":uptime}
    return pickle.dumps(data)

def sendStats(host,port,stats):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
        client.connect((host,port))
        client.sendall(stats)
        print("Datos enviados al servidor.")

host = '10.0.0.3'
port = 12345

while True:
    sendStats(host,port,getStats())
    time.sleep(30) 