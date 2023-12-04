from django.db import models

class property_listing(models.Model):
  property_listing_id=models.AutoField(primary_key=True)
  property_listing_date=models.DateField()
  property_listing_street=models.TextField()
  property_listing_city=models.TextField()
  property_listing_state = models.TextField()
  property_listing_zipcode = models.TextField()
  property_listing_price = models.DecimalField(max_digits=10,decimal_places=0)
  listing_description = models.TextField()
  property_listing_status = models.TextField()
  property_listing_is_featured = models.BooleanField()
  property_listing_pic1 = models.ImageField(null=True)
  property_listing_pic2 = models.ImageField(null=True)
  property_listing_pic3 = models.ImageField(null=True)
  property_listing_pic4 = models.ImageField(null=True)
  property_price_range_id = models.IntegerField()
  property_neighbourhood_id = models.IntegerField()
  admin_id = models.IntegerField()
  property_type_id = models.IntegerField()

class property_neighbourhood(models.Model):
    property_neighbourhood_id = models.AutoField(primary_key=True)
    property_neighbourhood_name = models.TextField()


class property_type(models.Model):
  property_type_id = models.AutoField(primary_key=True)
  property_type_name = models.TextField()


class property_price_range(models.Model):
  property_price_range_id = models.AutoField(primary_key=True)
  property_price_range = models.TextField()