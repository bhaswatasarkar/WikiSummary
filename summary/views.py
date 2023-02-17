from django.shortcuts import render
from django.http import HttpResponse
from .algorihms.sumy import func

def homePage(request):
    return render(request,'home.html')

def outputPage(request):
    func()
    return render(request,'output.html')