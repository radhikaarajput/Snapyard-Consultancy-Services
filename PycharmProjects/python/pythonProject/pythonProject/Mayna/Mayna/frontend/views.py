from django.shortcuts import render
from .models import *

def products(request):
    productss = Product.objects.all()
    return render(request, 'products.html', {'productss':productss})