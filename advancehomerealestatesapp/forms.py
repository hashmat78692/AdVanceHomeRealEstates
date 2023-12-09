# forms.py
from django import forms
from .models import Realtor, attraction
from .models import realtor_profile
class sendEmailForm(forms.Form):
      your_name = forms.CharField(required=True)
      your_email = forms.EmailField(required=True, label='Your email')
      message = forms.CharField(required=True, widget=forms.Textarea)


class realtorProfileForm(forms.ModelForm):
      class Meta:
            model = realtor_profile
            fields = ['first_name', 'last_name', 'realtor_img', 'email', 'phone_number', 'realtor_desc']


class attractionForm(forms.ModelForm):
      class Meta:
            model = attraction
            fields = ['attraction_name', 'attraction_desc', 'attraction_image', 'attraction_url', 'attraction_active']