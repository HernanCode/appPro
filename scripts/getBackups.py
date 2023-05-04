import os, datetime
date = datetime.datetime.now().strftime('%Y-%m-%d')


os.system(f'scp usuario@10.0.0.2:/home/samuel/backups/Completa-{date}.tar.gz /home/samuel/backups/10.0.0.2')
os.system(f'scp usuario@10.0.0.2:/home/samuel/backups/Diferencial-{date}.tar.gz /home/samuel/backups/10.0.0.2')
os.system(f'scp usuario@10.0.0.2:/home/samuel/backups/Incremental-{date}.tar.gz /home/samuel/backups/10.0.0.2')
os.system(f'scp usuario@10.0.0.3:/home/usuario/backups/Completa-{date}.tar.gz /home/samuel/backups/10.0.0.3')
os.system(f'scp usuario@10.0.0.3:/home/usuario/backups/Diferencial-{date}.tar.gz /home/samuel/backups/10.0.0.3')
os.system(f'scp usuario@10.0.0.3:/home/usuario/backups/Incremental-{date}.tar.gz /home/samuel/backups/10.0.0.3')