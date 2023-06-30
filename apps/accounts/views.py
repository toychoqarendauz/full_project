from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import CreateUserForm


def signup_page(request):
	form = CreateUserForm()
	if request.method == 'POST':
		form = CreateUserForm(request.POST)
		if form.is_valid():
			form.save()
			user = form.cleaned_data.get('username')
			messages.success(request, 'Account was created successfully!')
			return redirect('login_page')
	context = { 'form': form }
	return render(request, 'accounts/signup-page.html', context)


def login_page(request):
	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')
		user = authenticate(request, username=username, password=password)
		if user is not None:
			login(request, user)
			return redirect('home_page')
		else:
			messages.info(request, 'Username OR Password is incorrect')
	return render(request, 'accounts/login-page.html')


def logout_user(request):
	logout(request)
	return redirect('login_page')