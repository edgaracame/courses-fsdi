from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from .forms import RegisterUserForm
from django.contrib.auth import authenticate, login as alt_login

class SignUpView(CreateView):
    form_class = UserCreationForm
    template_name = "registration/signup.html"
    success_url = reverse_lazy("login")

def signup(request):
    if request.method == "POST":
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            alt_login(request, user)
            return redirect('home')
    else:
        form = RegisterUserForm()
    return render(request, 'registration/signup.html', {
        'form': form,
    })

def login(request):
    return render(request, 'registration/login.html', {})

def logout(request):
    return render(request, 'registration/logout.html', {})