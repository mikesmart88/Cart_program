from django.shortcuts import render, redirect 
from django.http import HttpRequest as hr ,JsonResponse as jr
from .models import phones , cart
from .cart import add_to_cart
from .fuctions import rand_string_generator

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

def phone(request):

    path = phones.objects.filter(pro_request=True).order_by('?').order_by('-post_date').all

    context = {
        'pro':path,
    }
    return render(request, 'testingapp/phones.html', context=context )

def profile(request, user_id):
    path = phones.objects.filter(verification_code__exact=user_id).first()

    context = {
        'name':path.Name,
        'brand':path.brand,
        'image':path.image,
        'des':path.description,
        'code':path.verification_code,
    }

    return render(request, 'testingapp/product_type.html',context=context)

def top_cart(request, user_id):

    path = phones.objects.get(verification_code__exact=user_id)

    if path:

         context ={
        'name':path.Name,
        'user_id':path.verification_code
    }

    check = cart.objects.create(
        Name = path.Name,
        description = path.description,
        brand = path.brand,
        price = path.price,
        image = path.image,
        color = path.color,
        currency = path.currency,
        operating_systerm = path.operating_systerm,
        Ram = path.Ram,
        memory = path.memory,
        cart_id = rand_string_generator(10),
        screen = path.screen,
        cellular_tech = path.cellular_tech,
        resolution = path.resolution,
        connectivity = path.connectivity,
        pro_request = path.pro_request,
        post_date = True
    )

    path.is_chart = True
    check.save()

    

    return redirect('/')
