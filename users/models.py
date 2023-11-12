from django.db import models
from django.contrib.auth.models import User
from PIL import Image
# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    First_Name = models.CharField(max_length = 25, null = True)
    Last_Name  = models.CharField(max_length = 25, null = True)
    image = models.ImageField(default='default.jpg',upload_to='profile_pics')
    Phone_Number = models.CharField(max_length=13, null=True)
    address = models.CharField(max_length = 50, null = True)
    Office_Email = models.EmailField(max_length = 50,null = True)

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, *args,**kwargs):
        super().save(*args,**kwargs)

        img = Image.open(self.image.path)

        if img.height > 300 or img.width >300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)