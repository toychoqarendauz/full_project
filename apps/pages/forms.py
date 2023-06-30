from django.forms import ModelForm
from .models import AddCar

class AddCarForm(ModelForm):
	class Meta:
		model = AddCar
		fields = '__all__'