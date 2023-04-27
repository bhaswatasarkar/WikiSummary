from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.homePage) ,
    path('summary', views.outputPage),
    path('analysis',views.analysisPage),
    path('getanalysis',views.getAnalysisPage),
]

