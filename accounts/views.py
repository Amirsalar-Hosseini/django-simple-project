from django.shortcuts import render, redirect
from .forms import RegisterForm, LoginForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = User.objects.create_user(cd['username'], cd['email'], cd['password'])
            user.firstname = cd['firstname']
            user.lastname = cd['lastname']
            user.save()
            messages.success(request, 'user registered successfully', 'success')
            return redirect('home')
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})


def login_page(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, username=cd['username'], password=cd['password'])
            if user is not None:
                login(request, user)
                messages.success(request, 'login successfully', 'success')
                return redirect('home')
            else:
                messages.error(request, 'username or password incorrect', 'danger')
                return redirect('login')
    else:
        form = LoginForm()
        return render(request, 'login.html', {'form': form})