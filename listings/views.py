# listings/views.py

from django.shortcuts import render, redirect,get_object_or_404
from .forms import ListingForm
from .models import Listing
from .forms import ListingSearchForm


def add_listing(request):
    if request.method == 'POST':
        form = ListingForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('listings:listing_list')
    else:
        form = ListingForm()

    return render(request, 'add_listing.html', {'form': form})

def listing_list(request):
    listings = Listing.objects.all()
    return render(request, 'listing_list.html', {'listings': listings})


def search_listings(request):
    # Handle form submission
    if request.method == 'GET':
        form = ListingSearchForm(request.GET)
        if form.is_valid():
            # Build the queryset based on form input
            queryset = Listing.objects.all()

            neighborhood = form.cleaned_data.get('neighborhood')
            if neighborhood:
                queryset = queryset.filter(neighborhood=neighborhood)

            price_range = form.cleaned_data.get('price_range')
            if price_range:
                queryset = queryset.filter(price_range=price_range)

            property_type = form.cleaned_data.get('property_type')
            if property_type:
                queryset = queryset.filter(property_type=property_type)

            # Pass the queryset to the template
            return render(request, 'search_listings.html', {'form': form, 'listings': queryset})

    # Render the initial form
    else:
        form = ListingSearchForm()

    return render(request, 'search_listings.html', {'form': form})

def listing_detail(request, listing_id):
    listing = get_object_or_404(Listing, pk=listing_id)



    return render(request, 'listing_detail.html',{'listing': listing})



