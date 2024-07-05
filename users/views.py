from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import redirect, render
from users.models import User

# Create your views here.
################ Authentication URLs ##############
def user_login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        print("This is a post request")
        user = authenticate(request, username=username, password=password)
        print(f"User: {user.email}")
        if user is not None:
            login(request, user)

            return redirect("home")
    return render(request, "accounts/login.html")


def user_logout(request):
    logout(request)
    return redirect("login")


def user_register(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        role = request.POST.get("role")
        phone_number = request.POST.get("phone_number")
        id_number = request.POST.get("id_number")
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        gender = request.POST.get("gender")
        email = request.POST.get("email")

        user = User.objects.create(
            username=username,
            email=email,
            role=role,
            phone_number=phone_number,
            id_number=id_number,
            first_name=first_name,
            last_name=last_name,
            gender=gender
        )

        user.set_password(password)
        user.save()
        return redirect("login")
    return render(request, "accounts/signup.html")