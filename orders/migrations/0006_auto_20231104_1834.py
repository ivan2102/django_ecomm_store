# Generated by Django 3.1 on 2023-11-04 17:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0005_auto_20231104_1828'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productorder',
            name='order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.order'),
        ),
    ]
