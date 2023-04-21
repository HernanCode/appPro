from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Server(models.Model):
    name = models.CharField(max_length=255)
    os = models.CharField(max_length=255)
    ip = models.CharField(max_length=255)
    adminUser = models.CharField(max_length=255)
    isAdministrated = models.ManyToManyField(User, through='Administrate')
    isActive = models.BooleanField(default=False)
    
    
class Administrate(models.Model):
    idUser = models.ForeignKey(User, on_delete=models.CASCADE)
    idServer = models.ForeignKey(Server, on_delete=models.CASCADE)



class Backup(models.Model):
    idServer = models.ForeignKey(Server, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    date = models.DateTimeField(auto_now_add=True)
    backupType = models.CharField(max_length=255) 
    
