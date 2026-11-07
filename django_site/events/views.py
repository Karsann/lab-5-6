from datetime import datetime
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import EventRegistrationForm

def index(request):
    context = {
        "title": "Головна сторінка подій",
        "events_count": 3,
        "organizer": "it hub ukraine",
        "year": datetime.now().year
    }
    return render(request, "events/index.html", context)

def events_list(request):
    events_data = [
        {"name": "Python Meetup Kyiv", "price": 0, "active": True},
        {"name": "AI Conference 2026", "price": 450, "active": True},
        {"name": "Frontend Web Workshop", "price": 200, "active": False}
    ]
    context = {
        "title": "Список подій",
        "events": events_data,
        "year": datetime.now().year
    }
    return render(request, "events/events.html", context)

def register(request):
    if request.method == "POST":
        form = EventRegistrationForm(request.POST)
        if form.is_valid():
            user_name = form.cleaned_data["name"]
            messages.success(request, f"Дякуємо, {user_name}! Ви успішно зареєструвалися.")
            return redirect("register")
    else:
        form = EventRegistrationForm()

    context = {
        "title": "Реєстрація на подію",
        "form": form,
        "year": datetime.now().year
    }
    return render(request, "events/register.html", context)

from django.shortcuts import render

# Create your views here.
