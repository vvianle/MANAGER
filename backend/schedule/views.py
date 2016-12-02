from datetime import date, datetime
from django.http import Http404
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .models import *
from .serializers import *
from accounts.permissions import *
from accounts.models import MyUser
from .utils.Generator import Generator
from .utils.PersonalSchedule import PersonalSchedule
from one_auth.authentication import OneTokenAuthentication
import json
from rest_framework.response import Response
from rest_framework import status

# GET /working/default/(?P<pk>\d+)/
# PUT /working/default/(?P<pk>\d+)/
class WorkingDefaultView(generics.RetrieveUpdateAPIView):
	serializer_class = WorkingDefaultSerializer
	permission_classes = (HasWorkingScheduleAndOwnerOrIsAdmin, )
	authentication_classes = (OneTokenAuthentication,)

	def get_object(self):
		pk = self.kwargs['pk']
		user = MyUser.objects.get(pk=pk)
		try:
			return PersonalDefaultWorkingRequest.objects.get(user=user)
		except PersonalDefaultWorkingRequest.DoesNotExist:
			raise Http404('User does not exist.')
	

# GET /working/add/(?P<pk>\d+)/
# POST /working/add/(?P<pk>\d+)/
class WorkingAddDayView(generics.ListCreateAPIView):
	def perform_create(self, serializer):
		pk = self.kwargs['pk']
		user = MyUser.objects.get(pk=pk)
		serializer.save(user=user, addDay=True)

	serializer_class = WorkingExceptionalDaySerializer
	permission_classes = (HasWorkingScheduleAndOwnerOrIsAdmin, )
	authentication_classes = (OneTokenAuthentication,)

	def get_queryset(self):
		pk = self.kwargs['pk']
		user = MyUser.objects.get(pk=pk)
		queryset = ExceptionalWorkingDay.objects.filter(user=user).filter(addDay=True)
		return queryset

# GET /working/cancel/(?P<pk>\d+)/
# POST /working/cancel/(?P<pk>\d+)/
class WorkingCancelDayView(generics.ListCreateAPIView):
	def perform_create(self, serializer):
		pk = self.kwargs['pk']
		user = MyUser.objects.get(pk=pk)
		serializer.save(user=user)

	serializer_class = WorkingExceptionalDaySerializer
	permission_classes = (HasWorkingScheduleAndOwnerOrIsAdmin, )
	authentication_classes = (OneTokenAuthentication,)

	def get_queryset(self):
		pk = self.kwargs['pk']
		user = MyUser.objects.get(pk=pk)
		queryset = ExceptionalWorkingDay.objects.filter(user=user).filter(addDay=False)
		return queryset

# GET /working/exceptional/(?P<pk>\d+)/(?P<date>\d{4}-\d{1,2}-\d{1,2})/
# DELETE /working/exceptional/(?P<pk>\d+)/(?P<date>\d{4}-\d{1,2}-\d{1,2})/
class WorkingSingleExceptionalDayView(generics.RetrieveDestroyAPIView):
	serializer_class = WorkingExceptionalDaySerializer
	permission_classes = (HasWorkingScheduleAndOwnerOrIsAdmin, )
	lookup_field = ('date')
	authentication_classes = (OneTokenAuthentication,)

	def get_queryset(self):
		pk = self.kwargs['pk']
		user = MyUser.objects.get(pk=pk)
		try:
			return ExceptionalWorkingDay.objects.filter(user=user)
		except ExceptionalWorkingDay.DoesNotExist:
			raise Http404('User does not exist.')

# GET /working/schedule/(?P<year>\d{4})/(?P<month>\d{1,2})/
class WorkingScheduleView(generics.RetrieveAPIView):
	serializer_class = WorkingScheduleSerializer
	permission_classes = (IsAdminOrReadOnly, )
	authentication_classes = (OneTokenAuthentication,)

	def get_object(self):
		month = int(self.kwargs['month'])
		year = int(self.kwargs['year'])
		try:
			return MonthlyWorkingSchedule.objects.filter(year=year).get(month=month)
		except MonthlyWorkingSchedule.DoesNotExist:
			raise Http404('Schedule does not exist')
		

# GET /working/personal/(?P<pk>\d+)/(?P<year>\d{4})/(?P<month>\d{1,2})/
# PUT /working/personal/(?P<pk>\d+)/(?P<year>\d{4})/(?P<month>\d{1,2})/
class PersonalWorkingScheduleView(generics.RetrieveAPIView):
	serializer_class = PersonalWorkingScheduleSerializer
	permission_classes = (HasWorkingScheduleAndOwnerOrIsAdmin, )
	authentication_classes = (OneTokenAuthentication,)

	def get_object(self):
		pk = self.kwargs['pk']
		user = MyUser.objects.get(pk=pk)
		month = int(self.kwargs['month'])
		year = int(self.kwargs['year'])
		try:
			return PersonalWorkingSchedule.objects.filter(user=user).filter(year=year).get(month=month)
		except PersonalWorkingSchedule.DoesNotExist:
			raise Http404('That personal schedule does not exist.')
		

# GET /working/generate/
# POST /working/generate/
class GenerateScheduleView(generics.ListCreateAPIView):

	def create(self, request, *args, **kwargs):
		serializer = self.get_serializer(data=request.data)
		serializer.is_valid(raise_exception=True)

		# if there is a startDate in request
		if 'startDate' in request.data and request.data['startDate'] != "":
			newDate = datetime.strptime(request.data['startDate'], '%Y-%m-%d').date()
			oldSchedule = MonthlyWorkingSchedule.objects.filter(month=newDate.month).get(year=newDate.year)
			
			# if that month already has a schedule available
			if oldSchedule:
				# generate a new schedule starting from that new date
				newSchedule = serializer.save(startDate=newDate)
				Generator().generator(newSchedule, newSchedule.startDate, False)
				newSchedule.save()

				# deserialized all schedule and calendar to update
				oCal = json.loads(oldSchedule.calendar.calendar)
				nCal = json.loads(newSchedule.calendar.calendar)
				oSche = json.loads(oldSchedule.schedule)
				nSche = json.loads(newSchedule.schedule)

				self.update_week(oCal, nCal, oSche, nSche, request.data['startDate'])

				# update old calendar and schedule according to new schedule
				start = False
				for week in range(0, len(oCal)):
					for day in range(0, len(oCal[week])):
						if oCal[week][day] == nCal[0][day] and oCal[week][day]!="":
							start = True
						if start:
							oCal[week][day] = nCal[len(nCal)-(len(oCal)-week)][day]
							oSche[week][day] = nSche[len(nSche)-(len(oSche)-week)][day]

				# save all new data to old schedule
				oldSchedule.calendar.calendar = json.dumps(oCal)
				oldSchedule.schedule = json.dumps(oSche)
				oldSchedule.nextStartDate = newSchedule.nextStartDate
				for worker in newSchedule.users.all():
					if worker not in oldSchedule.users.all():
						oldSchedule.users.add(worker)

				oldSchedule.calendar.save()
				oldSchedule.save()
				
				# and delete new schedule just created
				newSchedule.delete()
				newSchedule.calendar.delete()

				# delete all old personal schedule and generate new ones
				for personalSche in PersonalWorkingSchedule.objects.filter(month=newDate.month).filter(year=newDate.year):
					personalSche.delete()
				Generator().get_personal_schedule(newDate.year, newDate.month, oldSchedule.calendar, oCal, oSche, oldSchedule)

				# delete all schedule after this
				for schedule in MonthlyWorkingSchedule.objects.all():
					if schedule.month > oldSchedule.month:
						schedule.delete()

			else:
				# create new schedule starting from nextStartDate of previous month
				newSchedule = serializer.save(startDate=newDate, month=newDate.month, year=newDate.year)
				Generator().generator(newSchedule, newSchedule.startDate, True)
				newSchedule.save()
		else:
			lastSchedule = MonthlyWorkingSchedule.objects.last()
			if lastSchedule:
				newSchedule = serializer.save(startDate=lastSchedule.nextStartDate, month=lastSchedule.nextStartDate.month, year=lastSchedule.nextStartDate.year)
			# create new schedule starting from first day of following month
			else:
				month = date.today().month + 1
				year = date.today().year
				if month == 13:
					month = 1
					year = year + 1
				newDate = date(year, month, 1)
				newSchedule = serializer.save(startDate=newDate, month=newDate.month, year=newDate.year)
			Generator().generator(newSchedule, newSchedule.startDate, True)
			newSchedule.save()

		if len(WorkingCalendar.objects.all()) > 12:
			WorkingCalendar.objects.first().delete()

		return Response(serializer.data, status=status.HTTP_201_CREATED)

	def update_week(self, oCal, nCal, oSche, nSche, startDate):
		# update number of weeks in old schedule and calendar
		for week in range(0, len(oCal)):
			for day in range(0, len(oCal[0])):
				if oCal[week][day] == startDate:
					if (len(oCal) - week) == len(nCal):
						return
					elif (len(oCal) - week) > len(nCal):
						for n in range(len(oCal)-week-len(nCal)):
							oCal.pop(len(oCal)-1)
							oSche.pop(len(oSche)-1)
					else:
						for n in range(len(nCal)-(len(oCal)-week)):
							oCal.append(nCal[len(nCal)-1])
							oSche.append(nSche[len(nSche)-1])
					return


	serializer_class = WorkingScheduleSerializer
	permission_classes = (IsAdminUser, )
	queryset = MonthlyWorkingSchedule.objects.all()
	authentication_classes = (OneTokenAuthentication,)
		

# GET /working/schedule/current/
# PUT /working/schedule/current/
class CurrentWorkingScheduleView(generics.RetrieveUpdateAPIView):
	serializer_class = WorkingScheduleSerializer
	permission_classes = (IsAdminOrReadOnly, )
	authentication_classes = (OneTokenAuthentication,)

	def get_object(self):
		order = int(self.request.GET.get('order', None))
		try:
			return MonthlyWorkingSchedule.objects.order_by('-pk')[order]
		except IndexError:
			raise Http404('That working schedule does not exist.')

	def perform_update(self, serializer):
		serializer.save()
		schedule = self.get_object()

		# find all workers working this month
		working_users = []
		for week in json.loads(schedule.schedule):
			for day in week:
				if day != "" and day != "Holiday" and day != "OPEN":
					if ' | ' in day:
						check = day.split(' | ')
						for pp in check:
							if pp != "" and pp != "Holiday" and pp != "OPEN" and pp not in working_users:
								working_users.append(pp)
					elif day not in working_users:
						working_users.append(day)

		#update worker list
		for user in working_users:
			if MyUser.objects.get(username=user) not in schedule.users.all():
				schedule.users.add(MyUser.objects.get(username=user))

		# update their personal schedule
		for user in schedule.users.all():
			obj = PersonalWorkingSchedule.objects.get_or_create(user=user, calendar=schedule.calendar, month=schedule.month, year=schedule.year)[0]
			newSche = PersonalSchedule().personalSchedule(json.loads(schedule.calendar.calendar), json.loads(schedule.schedule), user.username)
			obj.personalSchedule = json.dumps(newSche)
			obj.save()

		#delete personal schedule if they are not working this month
		for personal in PersonalWorkingSchedule.objects.filter(month=schedule.month).filter(year=schedule.year):
			if personal.personalSchedule == '[]':
				personal.delete()


# GET /working/personal/current/(?P<pk>\d+)/
class PersonalCurrentWorkingScheduleView(generics.RetrieveAPIView):
	serializer_class = PersonalWorkingScheduleSerializer
	permission_classes = (HasWorkingScheduleAndOwnerOrIsAdmin, )
	authentication_classes = (OneTokenAuthentication,)

	def get_object(self):
		pk = self.kwargs['pk']
		user = MyUser.objects.get(pk=pk)
		order = int(self.request.GET.get('order', None))
		try:
			return PersonalWorkingSchedule.objects.filter(user=user).order_by('-pk')[order]
		except IndexError:
			raise Http404('That personal schedule does not exist.')
		



