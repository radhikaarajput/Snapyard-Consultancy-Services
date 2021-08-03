from django.shortcuts import render
from django.http import HttpResponse
from .models import Carausel
# Create your views here.
def index(request):
    return render(request, 'pages/layouts/base.html')

def plant(request):
    return render(request,'pages/layouts/plant.html')


def flowers(request):
    return render(request,'pages/layouts/flowers.html')

def subscription(request):
    return render(request,'pages/layouts/subscription.html')


def shantiCafe(request):
    return render(request,'pages/layouts/shantiCafe.html')

def blog(request):
    return render(request,'pages/layouts/blog.html')

def contact(request):
    return render(request,'pages/layouts/contact.html')


def ourStory(request):
    return render(request,'pages/layouts/ourStory.html')

def beSpoke(request):
    return render(request,'pages/layouts/beSpoke.html')
