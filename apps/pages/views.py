from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import AddCar
from .forms import AddCarForm


def landing_page(request):
	cars = AddCar.objects.all()
	context = { 'cars': cars }
	return render(request, 'pages/landing-page.html', context)


@login_required(login_url='login_page')
def home_page(request):
	cars = AddCar.objects.all()
	context = { 'cars': cars }
	return render(request, 'pages/home-page.html', context)


@login_required(login_url='login_page')
def rent_car(request):
	form = AddCarForm()
	cars = AddCar.objects.all()

	if request.method == 'POST':
		form = AddCarForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			return redirect('home_page')

	context = { 'form': form, 'cars': cars }
	return render(request, 'pages/rent-car-page.html', context)