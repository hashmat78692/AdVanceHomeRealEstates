"""
URL configuration for AdVanceHomeRealEstates project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.contrib import admin
from django.conf.urls.static import static
from django.urls import path, include

from listings import views as listing_views
from users import views as users_views
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('advancehomerealestatesapp.urls')),
    path('register/',users_views.register,name='register'),
    path('profile/',users_views.profile,name='profile'),
    path('listings/', listing_views.listings, name='listings'),
    path('save-listings', listing_views.savelistings, name='savelistings'),
    path('edit-listing/<int:id>', listing_views.editlistings, name='editlistings'),
    path('delete-listing/<int:id>', listing_views.deletelistings, name='deletelistings'),
    path('filter-listing', listing_views.filterlisting, name='filterlisting'),
    path('login/',auth_views.LoginView.as_view(template_name='users/login.html'),name='login'),
    path('logout/',auth_views.LogoutView.as_view(template_name='users/logout.html'),name='logout'),
    path('password-reset/',
     auth_views.PasswordResetView.as_view(template_name='users/password_reset.html'),
     name='password_reset'),
    path('password-reset/done',
     auth_views.PasswordResetDoneView.as_view(template_name='users/password_reset_done.html'),
     name='password_reset_done'),
    path('password-reset/confirm/<uidb64>/<token>/',
     auth_views.PasswordResetConfirmView.as_view(template_name='users/password_reset_confirm.html'),
     name='password_reset_confirm'),
    path('password-reset-complete/',
     auth_views.PasswordResetCompleteView.as_view(template_name='users/password_reset_complete.html'),
     name='password_reset_complete'),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)