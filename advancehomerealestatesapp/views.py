from django.shortcuts import render, redirect
from .forms import sendEmailForm
from django.http import HttpResponse
from django.core.mail import send_mail
from django.conf import settings

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
        email_form = sendEmailForm()
        #print(f"email_form: {email_form}")
        return render(request, 'advancehomerealestatesapp/contactUs.html', {'email_form':email_form})
