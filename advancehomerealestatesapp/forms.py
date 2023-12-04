# forms.py
from django import forms
from .models import Realtor
class sendEmailForm(forms.Form):
      your_name = forms.CharField(required=True)
      your_email = forms.EmailField(required=True, label='Your email')
      message = forms.CharField(required=True, widget=forms.Textarea)

