from django.shortcuts import render, redirect
from django.core.mail import send_mail
from .forms import ContactForm
from django.conf import settings

def home(request):
    return render(request, 'mrsregister/home.html', {'title': 'Welcome'})

def about(request):
    return render(request, 'mrsregister/about.html', {'title': 'About Us'})

def contact(request):
    if request.method == 'POST':
        # Get the data from the form
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        # Send the email
        send_mail(
            'New contact form submission',
            'Hello,\n\nYour message is being reviewed by the Module Registration team.\n\nName: {}\nEmail: {}\nMessage: {}\n'.format(name, email, message),
            'c0011865@outlook.com',
            [email],
            fail_silently=False
        )
   
    return render(request, 'mrsregister/contact.html', {'title': 'Contact Us'})

# Create your views here.
