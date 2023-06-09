# Generated by Django 4.1.7 on 2023-04-19 07:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Administrate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Server',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('os', models.CharField(max_length=255)),
                ('ip', models.CharField(max_length=255)),
                ('adminUser', models.CharField(max_length=255)),
                ('isAdministrated', models.ManyToManyField(through='dashboard.Administrate', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Backup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('backupType', models.CharField(max_length=255)),
                ('idServer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.server')),
            ],
        ),
        migrations.AddField(
            model_name='administrate',
            name='idServer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.server'),
        ),
        migrations.AddField(
            model_name='administrate',
            name='idUser',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
