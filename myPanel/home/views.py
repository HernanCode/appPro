from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout


# Create your views here.
def homePage(request):
    return render(request,'main.html')


def error_404(request,exception):
    return render(request,'404.html')


def loginPage(request):
    if request.user.is_authenticated:
        return redirect('../dashboard')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request,user)
                return redirect('../dashboard')
            else:
                error = True
                return render(request,'login.html',{'error':error})
        return render(request,'login.html')