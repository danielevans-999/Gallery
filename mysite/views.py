from django.shortcuts import render
from .models import Image

def home(request):
    images = Image.objects.all()
    return render(request,'mysite/home.html',{"images":images})

def search_results(request):
    if 'image' in request.GET and request.GET["image"]:

        search_term = request.GET.get("image")
        searched_Images = Image.search_image(search_term)
        message = f"{search_term}"

        return render(request, 'mysite/search.html', {"message": message, "Images": searched_Images})

    else:
        message = "You haven't searched for any term "
        return render(request, 'mysite/search.html', {"message": message})
