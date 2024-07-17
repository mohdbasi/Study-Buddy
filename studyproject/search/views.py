# views.py
from django.shortcuts import render
from .models import Item

def search(request):
    query = request.GET.get('q')
    if query:
        results = Item.objects.filter(name__icontains=query) | Item.objects.filter(description__icontains=query)
    else:
        results = Item.objects.all()
    return render(request, 'dashboard/search.html', {'results': results, 'query': query})

def add_example_items():
    Item.objects.create(name='Example Item 1', description='This is an example description for Item 1')
    Item.objects.create(name='Example Item 2', description='This is an example description for Item 2')
    Item.objects.create(name='Example Item 3', description='This is an example description for Item 3')

