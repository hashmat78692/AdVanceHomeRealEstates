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
