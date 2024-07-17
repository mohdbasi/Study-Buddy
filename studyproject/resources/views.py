from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Resource
from .forms import ResourceForm

def resource_list(request):
    resources = Resource.objects.all()
    return render(request, 'resources/resource_list.html', {'resources': resources})

def upload_resource(request):
    if request.method == 'POST':
        form = ResourceForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()  # Save the form data to the database
            return redirect('resources')  # Redirect to resource list page after successful upload
    else:
        form = ResourceForm()
    return render(request, 'resources/upload_resource.html', {'form': form})

def download_resource(request, resource_id):
    resource = Resource.objects.get(pk=resource_id)
    file_path = resource.file.path
    with open(file_path, 'rb') as f:
        response = HttpResponse(f.read())
        response['Content-Disposition'] = 'inline; filename=' + resource.name
        return response
