from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.contrib import messages

@login_required
def main(request):
    messages.success(request, "You have been logged in successfully!")  # Add this line
    return render(request, "dashboard/main.html")

@login_required
def room(request):
    return render(request, 'room/rooms.html')

@login_required
def progress(request):
    return render(request, 'dashboard/progress.html')

@login_required
def calender(request):
    return render(request, 'calendarapp/calendar.html')

@login_required
def search(request):
    return render(request, 'dashboard/search.html')

@login_required
def quiz(request):
    return render(request, 'quiz_app/quiz_list.html')

@login_required
def resources(request):
    return render(request, 'resources/resource_list.html')






