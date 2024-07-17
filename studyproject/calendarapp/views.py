# calendarapp/views.py
from django.shortcuts import render, redirect
from .models import Event
from .forms import EventForm

def calendar(request):
    events = Event.objects.all()
    return render(request, 'calendarapp/calendar.html', {'events': events})

def create_event(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('calendar')
    else:
        form = EventForm()
    return render(request, 'calendarapp/create_event.html', {'form': form})
