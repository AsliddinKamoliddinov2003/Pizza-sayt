from django.shortcuts import render,redirect
from  django.urls import reverse
from django.contrib.auth import authenticate, login

from .forms import *

def contact(request):
    form = UserContactForm()

    if request.method == "POST":
        form = UserContactForm(request.POST)
        
        if form.is_valid():
            form.save()
            return redirect(reverse("bosh-sahifa"))
    
    context = {
        "form":form
    }
            
    return render(request, "account/contact.html", context)


def register_user(request):
    form = UserRegisterForm()

    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse("login-user"))

    context = {
        "form":form
    }

    return render(request, "account/register.html", context)


def login_user(request):
    form = UserLoginForm()

    if request.method == "POST":
        form = UserLoginForm(request.POST)
        if form.is_valid():
            gmail = form.cleaned_data['gmail']
            password = form.cleaned_data['password']

            user = authenticate(request, gmail=gmail, password=password)

            if user:
                login(request, user=user)
                next = request.GET.get("next", None)
                if next :
                    return redirect(next)
                else:
                    return redirect(reverse("bosh-sahifa"))
            else:
                return redirect(reverse("login"))

    context = {
        "form":form
    }
    return render(request, "account/login.html", context)

    

def all_contact(request):
    contacts = Contact.objects.all()

    context = {
        "contacts":contacts
    }

    return render(request, "account/client.html", context)


def delete_contact(request, pk):
    try:
        contact  = Contact.objects.get(id=pk)
        contact.delete()
    except Contact.DoesNotExist:
        pass
    return redirect(reverse('all-contacts'))




        