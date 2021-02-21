from django.http import HttpResponse, HttpResponseRedirect
from django.core.mail import send_mail, BadHeaderError
from django.shortcuts import render, redirect
from .models import Contact


# Create your views here.

def home(request):
    return render(request, 'home.html', {})


def company(request):
    return render(request, 'company.html', {})


def services(request):
    return render(request, 'services.html', {})


def contact(request):
    if request.method == "POST":
        contact = Contact()
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        contact.name = name
        contact.email = email
        contact.subject = subject
        contact.save()
        return HttpResponse("<h1>THANKS FOR CONTACTING US!!</h1>")

    return render(request, "contact.html", {})
