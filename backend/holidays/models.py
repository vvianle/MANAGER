from django.db import models
from datetime import date

# Create your models here.
class Holiday(models.Model):
	"""
	Create a holiday range with startDate and endDate
	"""
	startDate = models.DateField(default=date.today())
	endDate = models.DateField(default=date.today())
	noLunch = models.BooleanField()
	noWorking = models.BooleanField()

	class Meta:
		unique_together=('startDate', 'endDate')

	def __str__(self):
		return str(self.startDate) + ' to ' + str(self.endDate)
