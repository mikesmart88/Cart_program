from django.shortcuts import render, redirect 
from django.http import HttpRequest as hr ,JsonResponse as jr
from .models import phones

# Create your views here.
#views for simple cart program

def home(request):
    path = phones.objects.filter(pro_request=True).order_by('?').order_by('-post_date')[:5]

    context = {
        'pro': path
    }
    return render(request, 'testingapp/home.html', context=context)
def base(request):
    return render(request, 'testingapp/base.html')
