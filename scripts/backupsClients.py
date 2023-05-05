import os, datetime

#Makes a full copy of the path list
def fullBackup(paths):
    date = datetime.datetime.now().strftime('%Y-%m-%d')
    pathToSave = f"/home/samuel/backups"
    command = f"tar -cf {pathToSave}/Completa-{date}.tar.gz " + " ".join(paths)
    print(command)
    os.system(command)
    
    
#Makes a differential copy of the path list
def diffBackup(paths):
    date = datetime.datetime.now().strftime('%Y-%m-%d')
    dateYearMonth = datetime.datetime.now().strftime('%Y-%m')
    pathToSave = f"/home/samuel/backups"
    command = f"tar -cpzf {pathToSave}/Diferencial-{date}.tar.gz " + "* ".join(paths) + " -N " + f"{dateYearMonth}-01"
    os.system(command)
    
#Makes a incremental copy of the path list
def incBackup(paths):
    date = datetime.datetime.now().strftime('%Y-%m-%d')
    pathToSave = f"/home/samuel/backups"
    command = f"tar -cpzf {pathToSave}/Incremental-{date}.tar.gz  -g {pathToSave}/backup.snap " + " ".join(paths)
    os.system(command)  


#Array that has the list of all paths 
paths = ["/home/samuel/Escritorio/backupspros"]

#fullBackup(paths)
#diffBackup(paths)
#incBackup(paths)
