from django.shortcuts import render,redirect,HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import *
from django.db.models import Q

# Create your views here.
def home(request):
    if request.method=="POST":
        msg=request.POST.get('message')
        p=product.objects.filter(Q(name_icontains=msg))
    else:
        p=product.objects.all()
    return render (request,'index.html',{'product':p})
def signupuser(request):
    choice=request.POST.get('option')
    if choice=='seller':
        s=seller()
        s.name=request.POST.get('name')
        s.uname=request.POST.get('uname')
        s.email=request.POST.get('email')
        pward=request.POST.get('password')   
        try:
            user=User.objects.create_user(username=s.name,email=s.email,password=pward)
            s.save()
            messages.success(request,'account created !! please try to login')
        except:
            messages.error(request,'username already exist please change user')
            return render(request,'login.html')
    else:
        b=buyer()
        b.name=request.POST.get('name')
        b.uname=request.POST.get('uname')
        b.email=request.POST.get('email')
        pward=request.POST.get('password')
        try:
            user=User.objects.create_user(username=b.name,email=b.email,password=pward)
            b.save()
            messages.success(request,'account created !! please try to login')
            return HttpResponseRedirect('/login')
        except:
            messages.error(request,'user already exist try again')
            return render(request,'login.html')

def logindetails(request):
    if request.method=="POST":
        uname=request.POST.get('uname')
        pward=request.POSt.get('password')
        user=User.authenticate(username=uname,password=pward)
        if user is not None:
            auth.login(request,user)
            return HttpResponseRedirect('/profile/')
        else:
            messages.error(request,'either username or password is incorrect')
    return render(request,'login.html')

        



