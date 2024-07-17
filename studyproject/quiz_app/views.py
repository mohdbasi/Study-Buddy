# quiz_app/views.py

from django.shortcuts import render
from django.contrib.auth.decorators import login_required



@login_required
def osquiz(request):
    return render(request, "quiz_app/quiz_temp/os.html")

@login_required
def coaquiz(request):
    return render(request, "quiz_app/quiz_temp/coa.html")

@login_required
def oopquiz(request):
    return render(request, "quiz_app/quiz_temp/oop.html")