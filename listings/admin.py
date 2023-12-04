from django.contrib import admin
from .models import Neighborhood
from .models import PropertyType
from .models import PriceRange
from .models import Listing
admin.site.register(Neighborhood)
admin.site.register(PropertyType)
admin.site.register(PriceRange)
admin.site.register(Listing)

# Register your models here.
