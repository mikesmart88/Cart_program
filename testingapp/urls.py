from django.urls import path
from . import views as v
from . import search as sr


app_name = 'testingapp'

urlpatterns = [
    path('',v.home, name='cart home' ) ,
    path('basedir',v.base, name='base dir') ,
    path('phones/', v.phone, name='phones') ,
    path('buy/<user_id>', v.profile, name='product_type') ,
    path('add_to_cart/', v.top_cart, name='adding to cart')  ,
]