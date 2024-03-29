from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group

# Create your views here.

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            
            #user_group = Group.objects.all()
            #user.groups.add(user_group)
            user = form.save()
            user.groups.add(form.cleaned_data.get('course'))
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}! Now you can login!')
            return redirect('login')
        else:
            messages.warning(request, 'Unable to create account!')
            return redirect('mrsregister:home')
    else:
        form = UserRegisterForm()
        return render(request, 'users/register.html', {'form': form , 'title': 'Student Registration'})

@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance = request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance = request.user.profile)
        if u_form.is_valid and p_form.is_valid:
            u_form.save()
            p_form.save()
            messages.success(request, 'Your account has been successfully updated')
        return redirect('profile')
    else:
        u_form = UserUpdateForm(instance = request.user)
        p_form = ProfileUpdateForm(instance = request.user.profile)
    context = {'u_form': u_form, 'p_form': p_form, 'title': 'Student Profile'}
    return render(request, 'users/profile.html', context)