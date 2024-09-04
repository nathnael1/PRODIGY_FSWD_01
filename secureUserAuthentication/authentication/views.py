from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.hashers import make_password, check_password
from django.core.validators import EmailValidator
from django.core.exceptions import ValidationError
from .models import user
def index(request):
    request.session['checker'] = False
    user_id = request.session.get('id')
    if request.session.get('user') == True:
        fullName = user.objects.get(id = user_id).fullName
        return render(request,"index.html",{ "fullName":fullName})
    return render(request,"unauthorized.html")
def login(request):
    if request.method == "POST":
        request.session.flush() 
        email = request.POST["email"]
        password = request.POST["password"]
        email_validator = EmailValidator()
        try:
            email_validator(email)
        except ValidationError:
            error = "Invalid email address"
            return render(request,"login.html",{"error":error})
        try:
            user_instance = user.objects.get(email = email)
        except user.DoesNotExist:
            error = "User not Found"
            return render(request,"login.html",{"error":error})
        if not check_password(password,user_instance.password):
            error = "Invalid password"
            return render(request,"login.html",{"error":error})
        request.session['user'] = True
        request.session['id'] = user_instance.id
        return HttpResponseRedirect(reverse("index"))
    request.session["user"] = False
    if request.session.get("checker") == True:
        return render(request,"login.html",{"success":"You are registered successfully"})
    return render(request,"login.html")
def register(request):
    if request.method == "POST":
        email = request.POST["email"]
        password = request.POST["password"]
        fullName = request.POST["fullName"]
        passwordConfirmation = request.POST["passwordConfirmation"]
        email_validator = EmailValidator()
        user_instance = user.objects.filter(email = email)
        if fullName == "":
            error = "Name cannot be empty"
            return render(request,"register.html",{"error":error})
        if user_instance:
            error = "User already exists"
            return render(request,"register.html",{"error":error})
            
        try:
            email_validator(email)
        except ValidationError:
            error = "Invalid email address"
            return render(request,"register.html",{"error":error})
        if password != passwordConfirmation:
            error = "Passwords do not match"
            return render(request,"register.html",{"error":error})
        if len(password) < 8:
            error = "Password should be at least 8 characters long"
            return render(request,"register.html",{"error":error})
        hashedPassword = make_password(password)
        new_user = user(email = email,password = hashedPassword,fullName = fullName)
        new_user.save()
        request.session["checker"] = True
        return HttpResponseRedirect(reverse("login"))
    request.session["user"] = False
    request.session["checker"] = False
    return render(request,"register.html")


