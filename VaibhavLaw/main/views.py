from django.shortcuts import render,redirect
from . forms import Contact_US_form
from django.contrib import messages
from . task import send_gmail
from celery import shared_task
from django.core.mail import send_mail
# Create your views here.
import time


def home(request):
      return render(request,"home.html")

def aboutus(request):
      return render(request,"aboutus.html")




def contact_us(request):
      if request.method == "POST":
            form = Contact_US_form(request.POST)
            if form.is_valid():
                        print(form.data)
                        form.save()
                        first_name = form.cleaned_data["first_name"]
                        last_name = form.cleaned_data["last_name"]
                        mobile_no = form.cleaned_data["mobile_no"]
                        email = form.cleaned_data["email"]
                        message = form.cleaned_data["message"]
                        name = first_name + " "+ last_name
                        global data
                        data = str(
                              {"Name" : name,"Email" : email,"Mobile Number" :  mobile_no, "Message" : message}
                              )
                        
                        send_gmail.delay(data)
                        messages.success(request, "Your message is recived. Thanks for contacting us, We will rich out to you shortly")
                        return redirect("contact_us")
            else:
                  print(form.errors)
                  return render(request,"contactus.html", {"form":form})
      else:
                  form = Contact_US_form()
                  return render(request,"contactus.html", {"form":form})

def carrers(request):
      return render(request,"carrers.html")

def practice_area(request):
      return render(request,"practice_area.html")

def ourvision(request):
      return render(request,"ourvision.html")



