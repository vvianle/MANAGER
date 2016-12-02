from django.db import models
from accounts.models import MyUser
from django.db.models.signals import post_save
from datetime import date
# Create your models here.

class ExceptionalLunchDay(models.Model):
	"""
	Create an additional day of register or cancel lunch with user, date.
	"""
	user = models.ForeignKey(MyUser, blank=True)
	date = models.DateField()
	addDay = models.BooleanField(default=False)

	class Meta:
		unique_together = ('user', 'date',)

	def __str__(self):
		return self.user.username + ' ' + str(self.date)


class PersonalDefaultLunchSchedule(models.Model):
	"""
	Each user's personal default lunch request.
	"""
	user = models.OneToOneField(MyUser, unique=True)
	mon = models.BooleanField(default=False)
	tue = models.BooleanField(default=False)
	wed = models.BooleanField(default=False)
	thu = models.BooleanField(default=False)
	fri = models.BooleanField(default=False)

	def __str__(self):
		return self.user.username

# each time a new user is created, create his personal default lunch request.
def new_worker_receiver(sender, instance, created, *args, **kwargs):
	if created:
		new_lunch, is_created = PersonalDefaultLunchSchedule.objects.get_or_create(user=instance)

post_save.connect(new_worker_receiver, sender=MyUser)


class DailyLunchRequest(models.Model):
	"""
	Daily lunch request with list of users and date.
	"""
	users = models.ManyToManyField(MyUser, blank=True)
	date = models.DateField(unique=True, null=True)
	totalOrders = models.IntegerField(default=0)
	price = models.IntegerField(null=True)
	calendar = models.ForeignKey('MonthCalendar', null=True)

	def __str__(self):
		return str(self.date)


class PersonalMonthlyLunchOrder(models.Model):
	"""
	Monthly personal lunch summary of each user - if user request a meal in that month.
	"""
	user = models.ForeignKey(MyUser)
	year = models.IntegerField()
	month = models.IntegerField()
	orderDays = models.CommaSeparatedIntegerField(max_length=400, null=True)
	numMeal = models.IntegerField(default=0)
	totalPrice = models.IntegerField(default=0)
	calendar = models.ForeignKey('MonthCalendar', null=True)

	class Meta:
		unique_together = ('user', 'month', 'year',)

	def __str__(self):
		return self.user.username + ' ' + str(self.year) +'-' + str(self.month)


class MealPrice(models.Model):
	"""
	Meal price with price and a startDate
	"""
	price = models.IntegerField(default=25000)
	inUse = models.BooleanField(default=False)
	startDate = models.DateField(default=date.today(), unique=True)

	def __str__(self):
		return str(self.startDate)


class MonthCalendar(models.Model):
	"""
	Calendar of each month.
	"""
	year = models.IntegerField()
	month = models.IntegerField()
	calendar = models.CharField(max_length=1000)

	class Meta:
		unique_together = ('year', 'month',)

	def __str__(self):
		return str(self.year) +'-'+ str(self.month)


