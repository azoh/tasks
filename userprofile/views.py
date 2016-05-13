from django.shortcuts import render_to_response, render
from django.http import HttpResponseRedirect
from django.core.context_processors import csrf
from . forms import UserProfileForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from . models import UserProfile
import random

def users(request):
    users = UserProfile.objects.all()
    return render(request, 'users.html', {
        'users' : users
        })

def user(request, user_id):
    return render_to_response('user.html', {'user': UserProfile.objects.get(id=user_id)})

def create_user(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/accounts/profile/')

    args = {}
    args.update(csrf(request))
    args['form'] = UserCreationForm

    return render_to_response('create_user.html', args)

def create_user_success(request):
    return HttpResponseRedirect('/accounts/profile/')

def user_profile(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/accounts/users')

    else:
        user = request.user
        profile = user.profile
        form = UserProfileForm(instance=profile)

    args = {}
    args.update(csrf(request))
    args['form'] = form

    return render_to_response('user_profie.html', args)
