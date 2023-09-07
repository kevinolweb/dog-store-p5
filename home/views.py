from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'home/index.html')

def newsletter(request):
    return render(request, 'newsletter.html')
