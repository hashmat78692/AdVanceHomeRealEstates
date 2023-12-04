from django.contrib import admin


from .models import *


class PropertyListing(admin.ModelAdmin):
  list_display = ("property_listing_id", "property_listing_date", "property_listing_street","property_listing_city",
                  "property_listing_state","property_listing_zipcode","property_listing_price","listing_description",
                  "property_listing_status","property_listing_is_featured"
                  ,"property_listing_pic1","property_listing_pic2","property_listing_pic3","property_listing_pic4",
                  "property_price_range_id","property_neighbourhood_id","admin_id","property_type_id")

admin.site.register(property_listing,PropertyListing)

class PropertyNeighbourhood(admin.ModelAdmin):
  list_display = ("property_neighbourhood_id","property_neighbourhood_name")

admin.site.register(property_neighbourhood,PropertyNeighbourhood)

class PropertyPriceRange(admin.ModelAdmin):
  list_display = ("property_price_range_id","property_price_range")

admin.site.register(property_price_range,PropertyPriceRange)

class PropertyType(admin.ModelAdmin):
  list_display = ("property_type_id","property_type_name")

admin.site.register(property_type,PropertyType)