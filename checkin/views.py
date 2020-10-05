from django.shortcuts import render, redirect
from django.core.mail import send_mail
from LALJI import settings
# Create your views here.
def home(request):
    if request.method == 'POST':
        if request.POST['first-name'] and request.POST['last-name'] and request.POST['email'] and request.POST['phone'] and request.POST['address'] and request.POST['rooms-adults'] and request.POST['rooms-kids'] and request.FILES['file']:
            subject = "New Web Check In"
            message = "Name:" + request.POST['first-name'] + " " + request.POST['last-name'] + ". Email ID: " + request.POST['email'] + "."
            to = "kkhanna1@jpischool.com"
            res = send_mail(subject, message, settings.EMAIL_HOST_USER, [to])
            return render(request, 'checkin/thankyou.html')




        else:
            return render(request, 'checkin/home.html', {'error':'Please fill all the details correctly'})
    else:
        return render(request, 'checkin/home.html')


def thankyou(request):
    return render(request, 'checkin/thankyou.html')
