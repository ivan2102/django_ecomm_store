# Generated by Django 3.1 on 2023-11-17 23:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_reviewrating'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductImageGallery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(max_length=255, upload_to='products/store')),
                ('products', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='products.product')),
            ],
            options={
                'verbose_name': 'productimagegallery',
                'verbose_name_plural': 'product image gallery',
            },
        ),
    ]
