# progress/views.py
from asyncio import Task
from django.shortcuts import render, redirect
from .models import Progress

def update_progress(request, task_id):
    if request.method == 'POST':
        progress = Progress.objects.get(pk=task_id)
        progress.progress_percent = request.POST.get('progress')
        progress.save()
        return redirect('progress', task_id=task_id)



def progress_details(request, task_id):
    # Logic to retrieve task details
    task = Task.objects.get(id=task_id)
    return render(request, 'dashboard/progress.html', {'task': task})
