from django.shortcuts import render, redirect
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, 'kenken.html')
def slider(request):
    return render(request, 'slider.html')
def tiles(request):
    return render(request, 'tiles.html')


