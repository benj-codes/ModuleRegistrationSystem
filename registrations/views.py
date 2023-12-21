from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from .models import Registration
from modules.models import Module

# Create your views here.

@login_required
def registrations(request, module_id):
    current_user = request.user
    module = Module.objects.get(id = module_id)
    registration = Registration(student=current_user, module = module)
    registration.save()
    return redirect('modules')
