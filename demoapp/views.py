from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.

def index(request):
    """
        Index for the app
    """
    return HttpResponse(f'<h1> Hello World </h1>')
