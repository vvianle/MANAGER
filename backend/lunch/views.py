from datetime import date
from django.core.mail import send_mail
from django.http import Http404
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .models import *
from .serializers import *
from .utils.LunchOrder import LunchOrder
from accounts.permissions import *
from accounts.models import MyUser
from one_auth.authentication import OneTokenAuthentication
from django.db.models.signals import post_save

# PUT /lunch/default/(?P<pk>\d+)/
# GET /lunch/default/(?P<pk>\d+)/
class LunchDefaultView(generics.RetrieveUpdateAPIView):

	def get_object(self):
		pk = self.kwargs['pk']
		user = MyUser.objects.get(pk=pk)
		try:
			return PersonalDefaultLunchSchedule.objects.get(user=user)
		except PersonalDefaultLunchSchedule.DoesNotExist:
			raise Http404('User does not exist.')

	serializer_class = LunchDefaultSerializer
	permission_classes = (IsOwnerOrAdmin, )
	authentication_classes = (OneTokenAuthentication,)

# POST /lunch/add/(?P<pk>\d+)/
# GET /lunch/add/(?P<pk>\d+)/
class LunchAddDayView(generics.ListCreateAPIView):
	def perform_create(self, serializer):
		pk = self.kwargs['pk']
		user = MyUser.objects.get(pk=pk)
		serializer.save(user=user, addDay=True)

	serializer_class = LunchExceptionalDaySerializer
	permission_classes = (IsOwnerOrAdmin, )
	authentication_classes = (OneTokenAuthentication,)

	def get_queryset(self):
		pk = self.kwargs['pk']
		user = MyUser.objects.get(pk=pk)
		queryset = ExceptionalLunchDay.objects.filter(user=user).filter(addDay=True)
		return queryset


# POST /lunch/cancel/(?P<pk>\d+)/
# GET /lunch/cancel/(?P<pk>\d+)/
class LunchCancelDayView(generics.ListCreateAPIView):
	def perform_create(self, serializer):
		pk = self.kwargs['pk']
		user = MyUser.objects.get(pk=pk)
		serializer.save(user=user)

	serializer_class = LunchExceptionalDaySerializer
	permission_classes = (IsOwnerOrAdmin, )
	authentication_classes = (OneTokenAuthentication,)

	def get_queryset(self):
		pk = self.kwargs['pk']
		user = MyUser.objects.get(pk=pk)
		queryset = ExceptionalLunchDay.objects.filter(user=user).filter(addDay=False)
		return queryset


# GET /lunch/exceptional/(?P<pk>\d+)/(?P<date>\d{4}-\d{2}-\d{2})/
# DELETE /lunch/exceptional/(?P<pk>\d+)/(?P<date>\d{4}-\d{2}-\d{2})/
class LunchSingleExceptionalDayView(generics.RetrieveDestroyAPIView):
	serializer_class = LunchExceptionalDaySerializer
	permission_classes = (IsOwnerOrAdmin, )
	lookup_field = ('date')
	authentication_classes = (OneTokenAuthentication,)

	def get_queryset(self):
		pk = self.kwargs['pk']
		user = MyUser.objects.get(pk=pk)
		try:
			return ExceptionalLunchDay.objects.filter(user=user)
		except ExceptionalLunchDay.DoesNotExist:
			raise Http404('User does not exist.')


# GET /lunch/day/(?P<date>\d{4}-\d{2}-\d{2})/
class DailyLunchRequestView(generics.RetrieveAPIView):
	serializer_class = LunchRequestSerializer
	permission_classes = (IsAuthenticated, ) 
	lookup_field = ('date')
	queryset = DailyLunchRequest.objects.all()
	authentication_classes = (OneTokenAuthentication,)


# GET /lunch/personal/(?P<pk>\d+)/(?P<year>\d{4})/(?P<month>\d{2})/
class PersonalMonthlyLunchView(generics.RetrieveAPIView):
	serializer_class = PersonalMonthlyLunchSerializer
	permission_classes = (IsOwnerOrAdmin, )
	authentication_classes = (OneTokenAuthentication,)

	def get_object(self):
		pk = self.kwargs['pk']
		user = MyUser.objects.get(pk=pk)
		month = int(self.kwargs['month'])
		year = int(self.kwargs['year'])
		try: 
			return PersonalMonthlyLunchOrder.objects.filter(user=user).filter(year=year).get(month=month)
		except PersonalMonthlyLunchOrder.DoesNotExist:
			raise Http404('That personal schedule does not exist.')


# GET /lunch/month/(?P<year>\d{4})/(?P<month>\d{2})/
class MonthlyLunchListView(generics.ListAPIView):
	serializer_class = PersonalMonthlyLunchSerializer
	permission_classes = (IsAuthenticated, )
	authentication_classes = (OneTokenAuthentication,)

	def get_queryset(self):
		month = int(self.kwargs['month'])
		year = int(self.kwargs['year'])
		return PersonalMonthlyLunchOrder.objects.filter(year=year).filter(month=month)


# GET /lunch/request/
# POST /lunch/request/
class EverydayLunchView(generics.ListCreateAPIView):
	def perform_create(self, serializer):
		if LunchOrder().isHoliday(date.today()):
			return
		else:
		# create daily lunch list, using utils to generate calendar and list people register
			newLunchRequest = serializer.save(date=date.today())
			LunchOrder().create_daily_lunch_list(newLunchRequest, date.today())
			newLunchRequest.save()

	serializer_class = LunchRequestSerializer
	permission_classes = (IsAdminUser, )
	queryset = DailyLunchRequest.objects.all()
	authentication_classes = (OneTokenAuthentication,)


def send_email(sender, instance, created, *args, **kwargs):
	if len(instance.users.all()) > 0:
		subject = '[MANAGER] Lunch Request '+ str(instance.date)
		message = ('All lunch request for today ('+ str(instance.date) +
			') has been made!\nPlease order ' + str(instance.totalOrders) +
			' meals for the following people:\n\n')
		for user in instance.users.all():
			message += user.username +' (email: ' + user.email + ')\n'
		message += '\nThe price is ' + str(instance.price) +' a meal.\n'
		message += 'Total price is ' + str(instance.price*len(instance.users.all())) + 'VND'
		for admin in MyUser.objects.filter(is_active=True).filter(is_admin=True):
			send_mail(subject, message, 'wmanager2016@gmail.com', [admin.email], fail_silently=False)

	if len(MonthCalendar.objects.all()) > 12:
		MonthCalendar.objects.first().delete()

post_save.connect(send_email, sender=DailyLunchRequest)


# GET /lunch/mealprice/
# POST /lunch/mealprice/
class MealPriceView(generics.ListCreateAPIView):
	serializer_class = MealPriceSerializer
	permission_classes = (IsAdminUser, )
	queryset = MealPrice.objects.all()
	authentication_classes = (OneTokenAuthentication,)


# GET /lunch/mealprice/(?P<startDate>\d{4}-\d{2}-\d{2})/
# DELETE /lunch/mealprice/(?P<startDate>\d{4}-\d{2}-\d{2})/
class SingleMealPriceView(generics.RetrieveDestroyAPIView):
	serializer_class = MealPriceSerializer
	permission_classes = (IsAdminUser, )
	lookup_field = ('startDate')
	authentication_classes = (OneTokenAuthentication,)
	queryset = MealPrice.objects.all()

# GET /lunch/current/
class CurrentLunchRequestView(generics.RetrieveAPIView):
	serializer_class = LunchRequestSerializer
	permission_classes = (IsAuthenticated, )
	authentication_classes = (OneTokenAuthentication,)

	def get_object(self):
		try:
			return DailyLunchRequest.objects.order_by('-pk')[0]
		except IndexError:
			raise Http404('That lunch request does not exist.')

# GET /lunch/month/current/
class CurrentMonthlyLunchListView(generics.ListAPIView):
	serializer_class = PersonalMonthlyLunchSerializer
	permission_classes = (IsAuthenticated, )
	authentication_classes = (OneTokenAuthentication,)

	def get_queryset(self):
		if len(PersonalMonthlyLunchOrder.objects.filter(year=date.today().year).filter(month=date.today().month)) > 0:
			return PersonalMonthlyLunchOrder.objects.filter(year=date.today().year).filter(month=date.today().month)
		else:
			if date.today().month == 1:
				return PersonalMonthlyLunchOrder.objects.filter(year=date.today().year-1).filter(month=12)
			else:
				return PersonalMonthlyLunchOrder.objects.filter(year=date.today().year).filter(month=date.today().month-1)

#GET /lunch/personal/current/(?P<pk>\d+)/
class PersonalCurrentMonthlyLunchView(generics.RetrieveAPIView):
	serializer_class = PersonalMonthlyLunchSerializer
	permission_classes = (IsOwnerOrAdmin, )
	authentication_classes = (OneTokenAuthentication,)

	def get_object(self):
		pk = self.kwargs['pk']
		user = MyUser.objects.get(pk=pk)
		try:
			return PersonalMonthlyLunchOrder.objects.filter(user=user).order_by('-pk')[0]
		except IndexError:
			raise Http404('User currently has no lunch summary or User does not exist.')

