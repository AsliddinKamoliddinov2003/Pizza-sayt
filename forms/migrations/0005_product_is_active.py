# Generated by Django 3.2.5 on 2021-08-20 18:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forms', '0004_product_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]
