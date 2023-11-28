from django.urls import path

from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('',views.index, name='home'),
    path('contactUs',views.about, name='contactUs'),
    path('contactUsView',views.contactUsView, name='contactUsView'),
]
