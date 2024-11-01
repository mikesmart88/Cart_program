from typing import Iterable
from django.db import models
from django.utils import timezone
from . import fuctions
from PIL import Image, ImageDraw, ImageFont
from io import BytesIO
import PIL
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.urls import reverse

# Create your models here.

class phones(models.Model):
    Name = models.CharField('Name of the phone product', max_length=50, blank=False)
    description = models.TextField('about the phone ', max_length=200, blank=False)
    image = models.ImageField('product image',null=False, blank=False)
    color = models.CharField('product color in text',null=False, max_length=100)
    visit = models.IntegerField('number of times visited pleas ignord this for it autumatically add it self', null=True, blank=True )
    price = models.IntegerField ('price of products', null=False, blank=False)
    currencych = [
    ('NGN', 'NGN'),
    ('USD', 'USD')
    ]
    currency = models.CharField(max_length=4, choices=currencych, null=True)
    discount = models.CharField('discount percentage to add to the products', null=True, blank=True, max_length=100)
    verification_code = models.CharField('please do not add this for it will add authomaticaly', blank=True, null= True ,unique=True, max_length=200)
    brand = models.CharField('product brand', null=False, blank=False, max_length=200)
    operating_systerm = models.CharField('products operating syayterm',null=False, blank=False, max_length=200)
    Ram = models.CharField ('ram memory installed size', blank=False, max_length=10)
    memory = models.CharField('memory storage capacity', max_length=20)
    screen = models.CharField('screen size, should end whit inches',max_length=5)
    cellular_tech = models.CharField('how many G is the products', max_length=20)
    resolution = models.CharField('products resolution', max_length=200)
    connectivity = models.CharField ('other connetivity eg bluetooth', max_length=200)
    is_chart = models.BooleanField('this will add authomaticaly pls do not cick', default=False)
    pro_request = models.BooleanField('click for product to be visible', default=False)
    post_date = models.DateTimeField('post date')
    is_auth = models.BooleanField(default=False)

    class Meta:
        ordering = ['-post_date']

    def __str__(self):
        if self.pro_request == True:
            return f'{self.Name} --- (published)'
        else:
            return f'{self.Name} --- (Draft)'
        

    def get_absolute_url(self):
        return reverse('testingapp:product_type', kwargs= { 'user_id':self.verification_code })

    def save(self , *args, **kwargs):
        if self.is_auth == False:
            self.verification_code = fuctions.rand_string_generator(10)
            self.is_auth = True
            if self.image :
                thum_img = Image.open(self.image)
                thum_img = thum_img.convert('RGB')
                i = thum_img

                i_io = BytesIO()
                i.save(i_io, format='PNG')
                self.image = InMemoryUploadedFile(i_io, None, f'{self.Name}{fuctions.rand_string_generator(5)}.jpg', 'image/jpg', None, None)

            else:
                pass
        else:
            pass

        return super(phones, self).save(*args, **kwargs)
    

class cart(models.Model):
        Name = models.CharField('Name of the phone product', max_length=50, blank=False)
        description = models.TextField('about the phone ', max_length=200, blank=False)
        image = models.ImageField('product image',null=False, blank=False)
        color = models.CharField('product color in text',null=False, max_length=100)
        visit = models.IntegerField('number of times visited pleas ignord this for it autumatically add it self', null=True, blank=True )
        price = models.IntegerField ('price of products', null=False, blank=False)
        currencych = [
        ('NGN', 'NGN'),
        ('USD', 'USD')
        ]
        currency = models.CharField(max_length=4, choices=currencych, null=True)
        discount = models.CharField('discount percentage to add to the products', null=True, blank=True, max_length=100)
        verification_code = models.CharField('please do not add this for it will add authomaticaly', blank=True, null= True ,unique=True, max_length=200)
        brand = models.CharField('product brand', null=False, blank=False, max_length=200)
        operating_systerm = models.CharField('products operating syayterm',null=False, blank=False, max_length=200)
        Ram = models.CharField ('ram memory installed size', blank=False, max_length=10)
        memory = models.CharField('memory storage capacity', max_length=20)
        screen = models.CharField('screen size, should end whit inches',max_length=5)
        cellular_tech = models.CharField('how many G is the products', max_length=20)
        resolution = models.CharField('products resolution', max_length=200)
        connectivity = models.CharField ('other connetivity eg bluetooth', max_length=200)
        pro_request = models.BooleanField('click for product to be visible', default=False)
        post_date = models.DateTimeField('post date')
        cart_id = models.CharField('cart id ', max_length=200, unique=True, null=True, blank=True)


    
        
