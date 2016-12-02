from django.db import models
from accounts.models import MyUser
from django.db.models.signals import post_save
from datetime import date


class MonthlyWorkingSchedule(models.Model):
	"""
	Monthly schedule of all users.
	"""
	users = models.ManyToManyField(MyUser, blank=True)
	startDate = models.DateField(null=True)
	month = models.IntegerField(null=True, default=0)
	year = models.IntegerField(null=True, default=0)
	calendar = models.ForeignKey('WorkingCalendar', null=True)
	schedule = models.CharField(max_length=1000, null=True)
	nextStartDate = models.DateField(null=True)

	class Meta:
		unique_together = ('month', 'year',)

	def __str__(self):
		return str(self.startDate)


class PersonalWorkingSchedule(models.Model):
	"""
	Personal schedule of each user each month.
	"""
	user = models.ForeignKey(MyUser)
	year = models.IntegerField()
	month = models.IntegerField()
	personalSchedule = models.CharField(max_length=500)
	calendar = models.ForeignKey('WorkingCalendar')

	class Meta:
		unique_together = ('user', 'month', 'year',)

	def __str__(self):
		return self.user.username + ' ' + str(self.year) +'-' + str(self.month)


class WorkingCalendar(models.Model):
	"""
	Working calendar each month.
	"""
	year = models.IntegerField()
	month = models.IntegerField()
	calendar = models.CharField(max_length=1000)

	def __str__(self):
		return str(self.year) +'-'+ str(self.month)


class ExceptionalWorkingDay(models.Model):
	"""
	Exceptional add/cancel working day of each user.
	"""
	user = models.ForeignKey(MyUser, blank=True)
	date = models.DateField()
	addDay = models.BooleanField(default=False)

	class Meta:
		unique_together = ('user', 'date',)

	def __str__(self):
		return self.user.username + ' ' + str(self.date)


class PersonalDefaultWorkingRequest(models.Model):
	"""
	Personal default working constraints of each user.
	"""
	user = models.OneToOneField(MyUser)
	sun_morning = models.BooleanField(default=False)
	sun_evening = models.BooleanField(default=False)
	mon = models.BooleanField(default=False)
	tue = models.BooleanField(default=False)
	wed = models.BooleanField(default=False)
	thu = models.BooleanField(default=False)
	fri = models.BooleanField(default=False)
	sat = models.BooleanField(default=False)
		
	def __str__(self):
		return self.user.username

def new_worker_receiver(sender, instance, created, *args, **kwargs):
	if created:
		new_worker, is_created = PersonalDefaultWorkingRequest.objects.get_or_create(user=instance)

post_save.connect(new_worker_receiver, sender=MyUser)


