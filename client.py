import socket
import psutil


def getStats():    
    cpuUsage = psutil.cpu_percent(4)
    ramUsage = round(psutil.virtual_memory()[3]/1000000000,1)
    return f'{cpuUsage}ñ{ramUsage}'


def sendStats(host,port,stats):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
        client.connect((host,port))
        message = stats.encode('utf-8')
        client.sendall(message)
        print("Datos enviados al servidor.")


host = '10.0.0.1'
port = 12345  

sendStats(host,port,getStats())
