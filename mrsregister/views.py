from django.shortcuts import render

def home(request):
    return render(request, 'mrsregister/home.html', {'title': 'Welcome'})

def about(request):
    return render(request, 'mrsregister/home.html', {'title': 'About Us'})

def contact(request):
    return render(request, 'mrsregister/home.html', {'title': 'Contact Us'})

# Create your views here.
