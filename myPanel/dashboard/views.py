from django.shortcuts import render, redirect
from .models import Server
from .forms import serverForm
import os 
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
import re

@login_required(login_url='login')
def serverCrud(request):
    servers = Server.objects.all()
    user = request.user
    firstname = request.user.first_name
    if request.method == 'POST':
        form = serverForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['nameServer']
            ip = form.cleaned_data['ipServer']
            adminUser = form.cleaned_data['adminUser']
            adminPassword = form.cleaned_data['adminPassword']
            path = form.cleaned_data['path']
            osServer = form.cleaned_data['osServer']
            if servers.filter(ip=ip).exists():
                showError = True
                error = "Ya existe esa ip, porfavor refresque la página :D"
                context = {'servers': servers, 'form': form,'firstname':firstname,"textError":error,'hasError':showError}
                return render(request, 'dashboard.html', context)
            if not serverStatus(ip):
                showError = True
                error = "Asegurese de que el servidor esté activo y visible en la red antes de añadirlo"
                context = {'servers': servers, 'form': form,'firstname':firstname,"textError":error,'hasError':showError}
                return render(request, 'dashboard.html', context)      
            dataServer = Server(name=name, ip=ip, os=osServer, adminUser=adminUser)
            dataServer.save()
            status = serverStatus(dataServer.ip)
            addServer(ip,osServer,adminUser,adminPassword,path,status) 
            return redirect('showDashboard')
    else:
        form = serverForm()
    for server in servers:
        status = serverStatus(server.ip)
        server.status = status
    
    context = {'servers': servers, 'form': form,'firstname':firstname}
    return render(request, 'dashboard.html', context)


def deleteServer(request, idServer):
    server = Server.objects.get(id=idServer)
    ip = server.ip
    backupsPath = f"/home/samuel/backups/{ip}"
    os.system(f"rm -rf {backupsPath}")
    os.system(f"rm -rf /home/samuel/appPro/myPanel/static/json/json-{ip}.json")
    server.delete()
    return redirect('showDashboard')


def serverStatus(ip):
    status = os.system(f"ping -c 1 {ip}")
    if status == 0:
        return True
    else:
        return False

def addServer(ip, oSystem, adminUser, adminPassword, pathToCopies,status):
    if not status:
        return None
    path = f"/home/{adminUser}/scripts"  
    command = f"sshpass -p {adminPassword} ssh-copy-id -f {adminUser}@{ip}"
    print(command)
    mkdirScripts = f"ssh {adminUser}@{ip} mkdir {path}" 
    sendFile = f"scp /home/samuel/appPro/scripts/client.py /home/samuel/appPro/scripts/backupsClients.py /home/samuel/appPro/scripts/Readme {adminUser}@{ip}:{path}"
    os.system(command)
    os.system(mkdirScripts)
    os.system(sendFile)

    backupsPath = f"/home/samuel/backups/{ip}"
    os.makedirs(backupsPath)
    os.system(f"cp /home/samuel/appPro/myPanel/static/json/default.json /home/samuel/appPro/myPanel/static/json/json-{ip}.json")
    with open("/home/samuel/appPro/scripts/getBackups.py","a") as file:
        print(file.writelines(f"\nos.system(f'scp {adminUser}@{ip}:{pathToCopies}/Completa-"+"{date}"+f".tar.gz {backupsPath}')"))
        print(file.writelines(f"\nos.system(f'scp {adminUser}@{ip}:{pathToCopies}/Diferencial-"+"{date}"+f".tar.gz {backupsPath}')"))
        print(file.writelines(f"\nos.system(f'scp {adminUser}@{ip}:{pathToCopies}/Incremental-"+"{date}"+f".tar.gz {backupsPath}')"))

def infoServer(request, idServer):
    server = Server.objects.get(id=idServer)
    ip = server.ip
    backupList = listBackups(ip)
    return render(request, 'serverPanel.html', {'server':server,'backups':backupList})


def userLogout(request):
    logout(request)
    return redirect('../login')


def getDate(file):
    dateRegex = r"\d{4}-\d{2}-\d{2}"
    return re.search(dateRegex, file).group()
    

def getType(file):
    wordRegex = r"\w+" 
    return re.search(wordRegex, file).group()


def getSize(ip, file):
    size = os.path.getsize(f"/home/samuel/backups/{ip}/{file}") / 1024 / 1024
    return round(size,2)

def listBackups(ip):
    route = f'/home/samuel/backups/{ip}' 
    listFiles = os.listdir(route)
    backupDict = {}
    for file in listFiles:
        backupDict[file] = {"type": getType(file), "size": getSize(ip, file), "date":getDate(file)}

    print(backupDict)
    return backupDict
