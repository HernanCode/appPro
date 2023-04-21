from django.shortcuts import render, redirect
from .models import Server
from .forms import serverForm
import os 



def serverCrud(request):
    servers = Server.objects.all()
    if request.method == 'POST':
        form = serverForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['nameServer']
            ip = form.cleaned_data['ipServer']
            adminUser = form.cleaned_data['adminUser']
            adminPassword = form.cleaned_data['adminPassword']
            os = form.cleaned_data['osServer']
            dataServer = Server(name=name, ip=ip, os=os, adminUser=adminUser)
            dataServer.save()
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
    