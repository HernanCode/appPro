from django.shortcuts import render

# Create your views here.
def homePage(request):
    return render(request,'main.html')


def error_404(request,exception):
    return render(request,'404.html')

