from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.forms import UserCreationForm
from accounts.forms import (
    RegistrationForm,

)
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User
# Create your views here.
def home(request):
    return redirect('/accounts/profile/')

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/accounts')
    else:
        form = RegistrationForm()

        args = {'form': form}
        return render(request, 'accounts/reg_form.html', args)


def view_profile(request):
    args = {'user': request.user}
    return render(request, 'accounts/profile.html', args)

def edit_profile(request):
    if request.method == 'POST':
        form = UserChangeForm(request.POST, instance=request.user)

        if form.is_valid():
            form.save()
            return redirect('accounts/profile')

    else:
        form = UserChangeForm(instance=request.user)
        args = {'form':form}
        return render(request, 'accounts/edit_profile.html', args)
