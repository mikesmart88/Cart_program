# Generated by Django 5.1.1 on 2024-10-10 20:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testingapp', '0005_phones_delete_apple_delete_products'),
    ]

    operations = [
        migrations.AlterField(
            model_name='phones',
            name='is_chart',
            field=models.BooleanField(default=False, verbose_name='this will add authomaticaly pls do not cick'),
        ),
        migrations.AlterField(
            model_name='phones',
            name='pro_request',
            field=models.BooleanField(default=False, verbose_name='click for product to be visible'),
        ),
    ]
