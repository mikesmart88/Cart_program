from django.shortcuts import render, redirect 
from django.http import HttpRequest as hr ,JsonResponse as jr

# Create your views here.
#views for simple cart program

def home(request):
    return render(request, 'testingapp/home.html')
def base(request):
    return render(request, 'testingapp/base.html')