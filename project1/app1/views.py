from django.shortcuts import render,redirect
from .forms import *
from .models import *
from django.contrib import messages
from django.contrib.auth import authenticate,login
from django.conf import settings
from django.core.mail import send_mail
# Create your views here.
def index(request):
    return render(request,'index.html')

def register(request):
    Rform = RegisterForm(request.POST)
    dict = {'Rform':Rform}
    if request.method == "POST":
        if Rform.is_valid():
            user=Rform.save()
            user.set_password(user.password)
            user.save()
            messages.success(request,"Registration successful..")
            return redirect('login')
        else:
            messages.error(request,'Invalid form submission..')
    return render(request,'Register.html',dict)

def login(request):
    Lform = LoginForm(request.POST)
    dict={'Lform':Lform}
    if request.method == "POST":
        uname = Lform['username'].value();
        pword = Lform['password'].value();
        user = authenticate(username=uname,password=pword)
        if user is not None:
            return redirect('index')
        else:
            messages.error(request, 'Incorrect username and / or password....')
            return render(request, 'Login.html',dict)
    return render(request,'Login.html',dict)
    