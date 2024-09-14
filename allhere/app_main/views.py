

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


# Create your views here.
@login_required(login_url="/users/login/")
def home_page(request):
    return render(request, "app_main/home.html")


@login_required(login_url="/users/login/")
def users_page(request):

    if not request.user.is_superuser:
        return redirect("/")

    users = User.objects.all()
    context = {
        "users": users
    }
    return render(request, "app_main/users.html", context)
