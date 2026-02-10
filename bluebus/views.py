from django.shortcuts import render
from .models import User
from .forms import Userregister
# Create your views here.

def Register(request):
    if request.method == "POST":
        form = Userregister(request.POST)
        if form.is_valid:
            form.save()
    else:
        form = Userregister()
    users = User.objects.all()
 
    return render(request,"registeruser.html",{
       "form" :form,
       "users":users
    })
