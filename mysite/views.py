from django.shortcuts import render
from .models import Image

def home(request):
    return render(request,'mysite/home.html')