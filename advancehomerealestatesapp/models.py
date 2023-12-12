# advancehomerealestatesapp/models.py

from django.contrib.auth.models import User
from django.db import models

class Realtor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    profile_image = models.ImageField(upload_to='realtor_profiles/', null=True, blank=True)

    def __str__(self):
        return self.user.username


# Create your models here.
class realtor_profile(models.Model):
    first_name = models.CharField(max_length=25,  null=False)
    last_name = models.CharField(max_length=25,  null=False)
    realtor_img = models.ImageField(upload_to='images/')
    realtor_desc = models.TextField(null=False)
    email = models.EmailField(max_length=254, null=False)
    phone_number = models.IntegerField(null=False)


class attraction(models.Model):
    attraction_name = models.CharField(max_length=25, null=False)
    attraction_image = models.ImageField(upload_to='images/')
    attraction_url = models.URLField(max_length=200, null=False)
    attraction_desc = models.TextField(null=False)
    attraction_active = models.BooleanField(null=False)
