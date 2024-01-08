from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Registration
from modules.models import Module
from django.shortcuts import render

# Create your views here.

# allow student to register for module
@login_required
def registrations(request, module_id):
    current_user = request.user
    module = Module.objects.get(id = module_id)
    registration = Registration(student=current_user, module = module)
    registration.save()
    messages.success(request, f'Thanks for registering for {module.name}! We hope you enjoy this module!')
    return redirect('modules')

@login_required
def unregister(request, module_id):
    current_user = request.user
    module = Module.objects.get(id = module_id)
    registration = Registration.objects.get(student=current_user, module = module)
    registration.delete()
    messages.success(request, f'You have unregistered {module.name}!')
    return redirect('modules')

@login_required
def myregistrations(request):
    current_user = request.user
    registrations = Registration.objects.filter(student=current_user)

    registrations_list = {'registrations': registrations, 'title': 'My Registrations'}

    return render(request, 'modules/myregistrations.html', registrations_list)
    
