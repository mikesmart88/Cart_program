from django.urls import path
from . import views as v

urlpatterns = [
    path('',v.home, name='cart home' ) ,
    path('basedir',v.base, name='base dir') ,
]