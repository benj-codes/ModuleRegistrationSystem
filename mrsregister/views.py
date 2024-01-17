from django.shortcuts import render
from django.core.mail import send_mail

def home(request):
    return render(request, 'mrsregister/home.html', {'title': 'Welcome'})

def about(request):
    return render(request, 'mrsregister/about.html', {'title': 'About Us'})

def contact(request):
    if request.method == "POST":
        message_username = request.POST['message-username']
        message_email = request.POST['message-email']
        message = request.POST['message']

        send_mail(
            'Message from ' + message_username, #subject
            message, #message
            message_email, #from email
            ['c0011865@hallam.shu.ac.uk'], #to email
        )

        
        return render(request, 'contact.html', {'message_username'})

    else:
        return render(request, 'mrsregister/contact.html', {'title': 'Contact Us'})

# Create your views here.
