from django.contrib import admin
from django.urls import include, path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.serverCrud,name='showDashboard'),
    path('deleteServer/<int:idServer>/', views.deleteServer, name='deleteServer')
    
]
