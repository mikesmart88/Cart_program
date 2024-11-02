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

def top_cart(request):
    try:
        if request.method == 'POST':
            cart_name = request.POST['name']
            cart_dex = request.POST['describ']
            cart_image = request.FILES['image']

            pin = cart.objects.create(
                Name = cart_name,
                description = cart_dex,
                image = cart_image
            )

            pin.save()

            return(jr({'S': 'new cart have been added'}, safe=False))
        else:
            return(jr({'W': 'sorry, only post request'}, safe=False))
        
    except BaseException as e:
        print(e)  
        return(jr({'E': 'sorry, something when wrong'}, safe=False))


