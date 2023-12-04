# listings/urls.py

from django.urls import path
from .views import add_listing,listing_list,search_listings,listing_detail

app_name = 'listings'

urlpatterns = [
    path('listing_list', listing_list, name='listing_list'),
    path('add_listing', add_listing, name='add_listing'),
    path('search_listings', search_listings, name='search_listings'),
    path('<int:listing_id>', listing_detail, name='listing_detail'),
    # Add more URLs as needed
]
