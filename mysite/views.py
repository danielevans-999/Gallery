from django.shortcuts import render
from .models import Image

def home(request):
    images = Image.objects.all()
    return render(request,'mysite/home.html' ,{"images":images})