# Generated by Django 3.0.4 on 2020-03-08 14:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='price_negotiability',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='item',
            name='sold',
            field=models.BooleanField(default=False),
        ),
    ]
