from django.shortcuts import render, HttpResponse
from HOME.models import Contact
from datetime import datetime

# Create your views here.

def index(request):
    return render(request, "index.html")
    #return HttpResponse("This is my page")
def about(request):
    return render(request, "about.html")    
    #return HttpResponse("About Section")
def contact(request): 
    if request.method == "POST":
        name = request.POST.get("Name")
        phone = request.POST.get("Phone")
        contact=Contact(Name=name, Phone=phone, Date=datetime.today())
        contact.save()
    return render(request, "contact.html")
    #return HttpResponse("Contact Section")

