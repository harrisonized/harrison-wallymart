from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    """ should put redirect here"""
    return HttpResponse("This is the regular homepage.") 

def index(request):
    return HttpResponse("This is the app homepage.")
