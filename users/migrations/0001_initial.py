# Generated by Django 4.2.4 on 2023-11-09 05:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('First_Name', models.CharField(max_length=25, null=True)),
                ('Last_Name', models.CharField(max_length=25, null=True)),
                ('image', models.ImageField(default='default.jpg', upload_to='profile_pics')),
                ('Phone_Number', models.CharField(max_length=13, null=True)),
                ('address', models.CharField(max_length=50, null=True)),
                ('Office_Email', models.EmailField(max_length=50, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
