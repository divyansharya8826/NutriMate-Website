from django.shortcuts import render, HttpResponse
from datetime import datetime
from home.models import Contact
from django.contrib import messages

# Create your views here.


def index(request):
    # context = {
    #     "variable1": "This is sent",
    # }
    return render(request, "index.html")
    # return HttpResponse("Hello, world. You're at the home page.")


def about(request):
    return render(request, "about.html")
    # return HttpResponse("Hello, world. You're at the about page.")


def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('message')
        contact = Contact(name=name, email=email, phone=phone,
                          desc=desc, date=datetime.today())
        contact.save()
        messages.success(request, "Your message has been sent!")
    return render(request, "contact.html")
    # return HttpResponse("Hello, world. You're at the contact page.")
