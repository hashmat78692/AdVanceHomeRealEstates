# listings/forms.py

from django import forms
from .models import Listing
from .models import Neighborhood, PriceRange, PropertyType

class ListingForm(forms.ModelForm):
    class Meta:
        model = Listing
        fields = ['image', 'neighborhood', 'property_type', 'price_range', 'price']


class ListingSearchForm(forms.Form):
    neighborhood = forms.ModelChoiceField(queryset=Neighborhood.objects.all(), empty_label='All Neighborhoods', required=False)
    price_range = forms.ModelChoiceField(queryset=PriceRange.objects.all(), empty_label='Any Price Range', required=False)
    property_type = forms.ModelChoiceField(queryset=PropertyType.objects.all(), empty_label='Any Property Type', required=False)

