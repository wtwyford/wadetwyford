from django.shortcuts import render

# Create your views here.

def index(request):

    name = request.GET.get('name', 'Guest')  # Default value is 'Guest'
    age = request.GET.get('age', 'Unknown') # Default value is 'Unknown'

    context = {}
    context['name'] = name
    context['age'] = age

    return render(request, 'homepage/index.html', context)

def about(request):
    return render(request, 'homepage/about.html', {})
