from django.db import models


class AddCar(models.Model):
	name = models.CharField(max_length=100)
	price = models.CharField(max_length=50)
	description = models.CharField(max_length=500)
	transmition = models.CharField(max_length=100, default='Manual')
	publication_date = models.DateTimeField(auto_now_add=True)
	image = models.ImageField(null=True, upload_to='images/')

	def __str__(self):
		return self.name