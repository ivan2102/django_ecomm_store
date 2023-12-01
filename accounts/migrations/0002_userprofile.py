# Generated by Django 3.1 on 2023-11-08 23:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(blank=True, max_length=100)),
                ('profile_picture', models.ImageField(blank=True, upload_to='userprofile,')),
                ('phone', models.CharField(blank=True, max_length=50)),
                ('city', models.CharField(blank=True, max_length=30)),
                ('state', models.CharField(blank=True, max_length=30)),
                ('country', models.CharField(blank=True, max_length=30)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
