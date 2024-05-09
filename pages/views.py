from django.shortcuts import render
from .models import *
# Create your views here.
from django.conf import settings
from django.http import HttpResponse

def home(request):
    return render(request,"index.html",{'DJANGO_SERVER_IP': settings.DJANGO_SERVER_IP})

def contact(request):
    if request.method=="POST":
        firstname=request.POST["firstname"]
        lastname=request.POST["lastname"]
        Email=request.POST["mail"]
        Phone_Number=request.POST["phone"]
        address=request.POST["local address"]
        state=request.POST["state"]
        postal=request.POST["postal code"]
        contact=counsel(first_name=firstname,email=Email,phone=Phone_Number,local_address=address,state=state,postal_code=postal,last_name=lastname)
        contact.save()
        return render(request,"contacts.html")
    return render(request,"contacts.html",{'DJANGO_SERVER_IP': settings.DJANGO_SERVER_IP})

def courses(request):
    return render(request,"courses.html",{'DJANGO_SERVER_IP': settings.DJANGO_SERVER_IP})
def blog(request):
    return render(request,"courses.html",{'DJANGO_SERVER_IP': settings.DJANGO_SERVER_IP})
def about(request):
    return render(request,"about.html",{'DJANGO_SERVER_IP': settings.DJANGO_SERVER_IP})

def FaQ(request):
    qna_data = [
        {"question": "Where can I find the bot?", "answer": "You can find it on our site under downloads."},
        {"question": "How do I install the app?", "answer": "You can download the installer from our website and follow the installation instructions."},
        {"question": "Can a normal person also use this site ", "answer": "Yes ,anyone can acess it but for the specially abled bot is given."},
        {"question": "What Type of courses offer", "answer": "Generally of class 10 , 12 and some coding language"},
        {"question": "Future plan ", "answer": "Generally of class 10 , 12 and some coding language"},
        # Add more Q&A pairs as needed
    ]
    return render(request, 'FaQ.html', {'qna_data': qna_data,'DJANGO_SERVER_IP': settings.DJANGO_SERVER_IP})
