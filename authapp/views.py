from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
import re


# Create your views here.



def signup(request):
    if request.method == "POST":
        name = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('Password1')
        confirm_password = request.POST.get('ConfirmPassword1')
       
        # validation
        flag=0
        if password!=confirm_password:
            messages.warning(request,"Password is not matching")
            redirect("/auth/signup/")
        elif len(password)<=8:
            messages.warning(request, "Password is too short ")
            redirect("/auth/signup/")
            
        elif not re.search('["a-z"]', password):
            flag = -1
            
        elif not re.search('["_@#$^&"]', password):
            flag = -1
            
        elif not re.search('["0-9"]', password):
            flag = -1
            
        elif re.search('["A-Z"]', password):
            flag = -1
        else:
            pass
        if flag == 0:
            try:
                if User.objects.get(username=email):
                    messages.info(request, "Email is already taken")
                    return redirect("/auth/signup/")
            except Exception as identifier:
                pass
            user = User.objects.create_user(email,email,password)
            user.first_name = name
            user.save()
            messages.success(request, "Signup Successfully, login here")
            return redirect("/auth/login/")
            
            
            
        else:
            messages.error(request,"Password must have a Special symbol, 0-9 ,a-z, A-Z")
            redirect("/auth/signup/")
    return render(request, "signup.html")

def handleLogin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        userpassword = request.POST.get('password')
        myuser = authenticate(username=username,password=userpassword)
        
        if myuser is not None:
            login(request, myuser)
            messages.success(request, "Login Successfully")
            return redirect("/home/")
        else:
            messages.error(request, "Invalid credentials")
            return redirect("/auth/login/")
    
    return render(request, "login.html")

def handleLogout(request):
    logout(request)
    messages.success(request,"Logout successfully")
    return render(request, "login.html")


