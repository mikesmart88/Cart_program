# Generated by Django 5.1.1 on 2024-09-27 12:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('testingapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='products',
            name='can be image or text',
        ),
    ]
