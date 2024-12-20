# Generated by Django 5.1.1 on 2024-10-20 21:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testingapp', '0009_phones_currency'),
    ]

    operations = [
        migrations.CreateModel(
            name='cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=50, verbose_name='Name of the phone product')),
                ('description', models.TextField(max_length=200, verbose_name='about the phone ')),
                ('image', models.ImageField(upload_to='', verbose_name='product image')),
                ('color', models.CharField(max_length=100, verbose_name='product color in text')),
                ('visit', models.IntegerField(blank=True, null=True, verbose_name='number of times visited pleas ignord this for it autumatically add it self')),
                ('price', models.IntegerField(verbose_name='price of products')),
                ('currency', models.CharField(choices=[('NGN', 'NGN'), ('USD', 'USD')], max_length=4, null=True)),
                ('discount', models.CharField(blank=True, max_length=100, null=True, verbose_name='discount percentage to add to the products')),
                ('verification_code', models.CharField(blank=True, max_length=200, null=True, unique=True, verbose_name='please do not add this for it will add authomaticaly')),
                ('brand', models.CharField(max_length=200, verbose_name='product brand')),
                ('operating_systerm', models.CharField(max_length=200, verbose_name='products operating syayterm')),
                ('Ram', models.CharField(max_length=10, verbose_name='ram memory installed size')),
                ('memory', models.CharField(max_length=20, verbose_name='memory storage capacity')),
                ('screen', models.CharField(max_length=5, verbose_name='screen size, should end whit inches')),
                ('cellular_tech', models.CharField(max_length=20, verbose_name='how many G is the products')),
                ('resolution', models.CharField(max_length=200, verbose_name='products resolution')),
                ('connectivity', models.CharField(max_length=200, verbose_name='other connetivity eg bluetooth')),
                ('pro_request', models.BooleanField(default=False, verbose_name='click for product to be visible')),
                ('post_date', models.DateTimeField(verbose_name='post date')),
                ('cart_id', models.CharField(blank=True, max_length=200, null=True, unique=True, verbose_name='cart id ')),
            ],
        ),
    ]
