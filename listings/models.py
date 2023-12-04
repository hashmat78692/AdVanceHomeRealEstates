from django.db import models

# Create your models here.
# listings/models.py

from django.db import models

class Neighborhood(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class PropertyType(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class PriceRange(models.Model):
    range_name = models.CharField(max_length=100)
    min_price = models.DecimalField(max_digits=10, decimal_places=2)
    max_price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.range_name} ({self.min_price} - {self.max_price})"

class Listing(models.Model):
    image = models.ImageField(upload_to='listing_images/')
    neighborhood = models.ForeignKey(Neighborhood, on_delete=models.CASCADE)
    property_type = models.ForeignKey(PropertyType, on_delete=models.CASCADE)
    price_range = models.ForeignKey(PriceRange, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    address = models.CharField(max_length=170, blank=True, null=True)

    def __str__(self):
        return f"{self.neighborhood} - {self.property_type} - ${self.price_range} - ${self.price}"
