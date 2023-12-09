from django.urls import path

from . import views
from django.contrib.auth import views as auth_views



urlpatterns = [
    path('',views.index, name='home'),
    path('contactUs',views.about, name='contactUs'),
    path('contactUsView',views.contactUsView, name='contactUsView'),
    path('editRealtorProfile/<int:pk>/',views.editRealtorProfile, name='editRealtorProfile'),
    path('attraction_list',views.attraction_list, name='attraction_list'),
    path('add_attraction', views.add_attraction, name='add_attraction'),
    path('edit_attraction/<int:pk>/',views.edit_attraction, name='edit_attraction'),



]
