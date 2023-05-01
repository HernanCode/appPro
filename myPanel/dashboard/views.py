from django.shortcuts import render, redirect
from .models import Server
from .forms import serverForm
import os 
import asyncio
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


@login_required(login_url='login')
def serverCrud(request):
    servers = Server.objects.all()
    if request.method == 'POST':
        form = serverForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['nameServer']
            ip = form.cleaned_data['ipServer']
            adminUser = form.cleaned_data['adminUser']
            adminPassword = form.cleaned_data['adminPassword']
            osServer = form.cleaned_data['osServer']
            dataServer = Server(name=name, ip=ip, os=osServer, adminUser=adminUser)
            dataServer.save()
            addServer(ip,osServer,adminUser,adminPassword) 
            return redirect('showDashboard')
    else:
        form = serverForm()
    
    for server in servers:
        status = serverStatus(server.ip)
        if status:
            server.status = True
        else:
            server.status = False    
    context = {'servers': servers, 'form': form}
    return render(request, 'dashboard.html', context)


def deleteServer(request, idServer):
    server = Server.objects.get(id=idServer)
    server.delete()
    return redirect('showDashboard')


def serverStatus(ip):
    status = os.system(f"ping -c 1 {ip}")
    if status == 0:
        return True
    else:
        return False

import os
def addServer(ip, oSystem, adminUser, adminPassword):
    path = f"/home/{adminUser}/scripts"  
    command = f"sshpass -p {adminPassword} ssh-copy-id -f {adminUser}@{ip}"
    print(command)
    mkdirScripts = f"ssh {adminUser}@{ip} mkdir {path}" 
    sendFile = f"scp /home/samuel/appPro/myPanel/dashboard/localScript.py {adminUser}@{ip}:{path}"
    os.system(command)
    os.system(mkdirScripts)
    os.system(sendFile)


def infoServer(request, idServer):
    server = Server.objects.get(id=idServer)
    return render(request, 'serverPanel.html', {'server':server})


def userLogout(request):
    logout(request)
    return redirect('../login')