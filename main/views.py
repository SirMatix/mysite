from asyncio.windows_events import NULL
from audioop import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from .forms import EventForm, NewUserForm
from django.views import generic
from django.utils.safestring import mark_safe

from .models import *
from .utils import Calendar





import calendar
from calendar import HTMLCalendar
from datetime import date, datetime, timedelta

# Create your views here.
def homepage(request):
    template_name = "main/home.html"
    return render(request,template_name, { "page_name": "Home"})


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


""" def calendar_view(request):
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
            "page_name": "View Calendar",
        }) """

class CalendarView(generic.ListView):
    model = Event
    template_name = 'main/calendar.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # use today's date for the calendar
        #d = get_date(self.request.GET.get('day', None))
        d = get_date(self.request.GET.get('month', None))
        context['prev_month'] = prev_month(d)
        context['next_month'] = next_month(d)

        # Instantiate our calendar class with today's year and date
        cal = Calendar(d.year, d.month)

        # Call the formatmonth method, which returns our calendar as a table
        html_cal = cal.formatmonth(withyear=True)
        context['calendar'] = mark_safe(html_cal)
        context['year'] = d.year
        context['month'] = calendar.month_name[d.month]
        context['page_name'] = 'Calendar'

        return context

def prev_month(d):
    first = d.replace(day=1)
    prev_month = first - timedelta(days=1)
    month = 'month=' + str(prev_month.year) + '-' + str(prev_month.month)
    return month

def next_month(d):
    days_in_month = calendar.monthrange(d.year, d.month)[1]
    last = d.replace(day=days_in_month)
    next_month = last + timedelta(days=1)
    month = 'month=' + str(next_month.year) + '-' + str(next_month.month)
    return month

def get_date(req_day):
    if req_day:
        year, month = (int(x) for x in req_day.split('-'))
        return date(year, month, day=1)
    return datetime.today()

def event(request, event_id=None):
    instance = Event()
    if event_id:
        instance = get_object_or_404(Event, pk=event_id)
    else:
        instance = Event()
    
    form = EventForm(request.POST or None, instance=instance)
    if request.POST and form.is_valid():
        form.save()
        return redirect("main:calendar")
        
    return render(request, 'main/event.html', {'form': form})

def events(request):
    current_user = request.user
    if current_user.is_authenticated:
        events = Event.objects.filter(owner=current_user.id)
        return render(request, 'main/events.html', {'events': events,
                                                     'page_name': 'Events List'})
    else:
        return render(request, 'main/wrong.html')    
    return NULL

def view_clients(request):
    current_user = request.user
    if current_user.is_authenticated:
        clients = Client.objects.filter(advisor=current_user.id)
        return render(request, 'main/clients.html', {'clients': clients,
                                                     'page_name': 'Clients List'})
    else:
        return render(request, 'main/wrong.html')
    