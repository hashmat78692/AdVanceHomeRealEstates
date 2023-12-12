from django.shortcuts import render, redirect,get_object_or_404
from .forms import sendEmailForm
from .forms import attractionForm
from django.http import HttpResponse
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth.decorators import login_required
from .models import realtor_profile, attraction
from .forms import realtorProfileForm

# Create your views here.
def index(request):
    return render(request,"advancehomerealestatesapp/index.html")


def about(request):
    #return render(request, "advancehomerealestatesapp/contactUs.html")
    return redirect(contactUsView)

def contactUsView(request):
    if request.method == 'POST':
        # POST, generate form with data from the request
        email_form = sendEmailForm(request.POST)
        # check if it's valid:
        if email_form.is_valid():
            # process data, insert into DB, generate email,etc
            # redirect to a new url:

            name = email_form.cleaned_data['your_name']
            email = email_form.cleaned_data['your_email']
            message = email_form.cleaned_data['message']

            text = f" {name}, {email}, {message}"
            print(f"Form data: {text}")
            email_message = f'Customer Name: {name}\nCustomer Email: {email}\nCustomer Message: {message}\n'
            print(text)
            sub = f"Contact Customer {name}"
            send_mail(subject=sub, message=email_message, from_email=settings.EMAIL_HOST_USER,
                      recipient_list=['tbano@unomaha.edu'])

            #return HttpResponse(text)
            return render(request, "advancehomerealestatesapp/emailSent.html")
    else:
        # GET, generate blank form
        profile_details = realtor_profile.objects.first()
        email_form = sendEmailForm()
        #print(f"email_form: {email_form}")
        return render(request, 'advancehomerealestatesapp/contactUs.html', {'email_form':email_form, 'profile_details': profile_details})


def editRealtorProfile(request, pk):
    profile = get_object_or_404(realtor_profile, pk=pk)

    if request.method == 'POST':
        form = realtorProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('contactUs')  # Redirect to the profile detail view after editing
    else:
        form = realtorProfileForm(instance=profile)
        return render(request, 'advancehomerealestatesapp/editRealtorProfile.html', {'form': form})
# return render(request, "advancehomerealestatesapp/contactUs.html")

def add_attraction(request):
    if request.method == 'POST':
        form = attractionForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('attraction_list')
    else:
        form = attractionForm()
        return render(request, 'add_attraction.html', {'form': form})

def attraction_list(request):
    attractions = attraction.objects.filter(attraction_active=True)
    return render(request, 'attraction_list.html', {'attractions': attractions})

def edit_attraction(request, pk):
    att = get_object_or_404(attraction, pk=pk)

    if request.method == 'POST':
        form = attractionForm(request.POST, request.FILES, instance=att)
        if form.is_valid():
            form.save()
            return redirect('attraction_list')  # Redirect to the profile detail view after editing
    else:
        form = attractionForm(instance=att)
        return render(request, 'advancehomerealestatesapp/edit_attraction.html', {'form': form})

