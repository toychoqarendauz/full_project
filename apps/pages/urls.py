from django.urls import path
from . import views


urlpatterns = [
	path('', views.landing_page, name='landing_page'),
	path('home/', views.home_page, name='home_page'),
	path('rent-car/', views.rent_car, name='rent_car'),
]
