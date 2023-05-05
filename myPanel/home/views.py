from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout


#Return html of a mainpage
def homePage(request):
    return render(request,'main.html')

#Error 404 if the  page not exists
def error_404(request,exception):
    return render(request,'404.html')

#Login function that authenticate username and password 
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