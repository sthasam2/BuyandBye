# Generated by Django 3.0 on 2020-01-02 14:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0002_auto_20200102_2028'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='slug',
        ),
        migrations.RemoveField(
            model_name='item',
            name='slug',
        ),
    ]
