import os, datetime

def fullBackup(paths):
    date = datetime.datetime.now().strftime('%Y-%m-%d')
    pathToSave = f"/home/samuel/backups"
    command = f"tar -cf {pathToSave}/Completa-{date}.tar.gz " + " ".join(paths)
    print(command)
    os.system(command)

def diffBackup(paths):
    date = datetime.datetime.now().strftime('%Y-%m-%d')
    dateYearMonth = datetime.datetime.now().strftime('%Y-%m')
    pathToSave = f"/home/samuel/backups"
    command = f"tar -cpzf {pathToSave}/Diferencial-{date}.tar.gz " + "* ".join(paths) + " -N " + f"{dateYearMonth}-01"
    os.system(command)

def incBackup(paths):
    date = datetime.datetime.now().strftime('%Y-%m-%d')
    pathToSave = f"/home/samuel/backups"
    command = f"tar -cpzf {pathToSave}/Incremental-{date}.tar.gz  -g {pathToSave}/backup.snap " + " ".join(paths)
    os.system(command)  

path = ["/home/samuel/Escritorio/backupspros/"]



