# Generated by Django 3.1 on 2023-11-03 23:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productorder',
            name='color',
        ),
        migrations.RemoveField(
            model_name='productorder',
            name='size',
        ),
    ]
