from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from .forms import NewUserForm
import calendar
from calendar import HTMLCalendar
from datetime import datetime

# Create your views here.
def homepage(request):
    template_name = "main/home.html"
    return render(request,template_name)


def register(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get("username")
            messages.success(request, f"New Account Created: {username}")
            login(request, user)
            messages.info(request, f"You are now logged in as {username}")
            return redirect("main:homepage")
        else:
            for msg in form.error_messages:
                messages.error(request, f"{msg}: {form.error_messages[msg]}")

    form = NewUserForm
    context = {"form": form}
    template_name= "main/register.html"
    return render(request, template_name, context)


def logout_request(request):
    logout(request)
    messages.info(request, "Logged out succesffully")
    return redirect("main:homepage")

def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}")
                return redirect("main:homepage")
            else:
                messages.error(request, "Invalid username or password")
        else:
                messages.error(request, "Invalid username or password")

    form = AuthenticationForm()
    return render(request, 
                  "main/login.html",
                  {"form":form})


def calendar_view(request):
    year = datetime.now().year
    month = datetime.now().strftime('%B')
    month_number = list(calendar.month_name).index(month)
    month_number = int(month_number)

    cal = HTMLCalendar().formatmonth(year,month_number)

    return render(
        request,
        "main/calendar.html",
        {
            "year": year,
            "month": month,
            "cal": cal,
        })
