# Generated by Django 3.2.5 on 2021-08-20 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forms', '0003_product_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='price',
            field=models.FloatField(default=5000),
        ),
    ]
