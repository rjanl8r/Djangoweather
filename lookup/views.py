from django.shortcuts import render

# Create your views here.

def home(request): #parameter is what the user types into the webscreen
    return render(request, 'home.html', {})


def about(request): #parameter is what the user types into the webscreen
    return render(request, 'about.html', {})