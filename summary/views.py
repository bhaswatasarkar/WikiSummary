from django.shortcuts import render
from django.http import HttpResponse
from .algorihms.transformer import *

def homePage(request):
    return render(request,'home.html')

def outputPage(request):
    base_url = "https://en.wikipedia.org/wiki/History_of_India"
    print(transformers_t5_base(base_url))
    return render(request,'output.html')

 