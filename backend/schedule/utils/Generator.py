from datetime import timedelta, date
import copy
import json
from accounts.models import MyUser
from holidays.models import Holiday
from schedule.models import *
from .Calendar import Calendar
from .Employee import Employee
from .Schedule import Schedule
from .PersonalSchedule import PersonalSchedule

# generate monthly working schedule
class Generator(object):

	def generator(self,newSchedule, startDate, isNew):
		# validate all holidays
		holidays = self.get_holidays()
		# get list of workers and their constraints
		workers = self.check_workers(newSchedule)
		
		# generate month working calendar, schedule and serialize it
		calendar = Calendar(startDate, holidays, workers, newSchedule).launch()
		schedule = Schedule(calendar['calendar'], workers, holidays, startDate, calendar['numShifts']).launch()

		serialized_calendar = self.serialize_calendar(calendar['calendar'])

		# create working calendar object
		monthCalendar = WorkingCalendar.objects.create(month=startDate.month, year=startDate.year, calendar=serialized_calendar)

		# generate personal schedule for each workers
		if (isNew):
			self.get_personal_schedule(startDate.year, startDate.month, monthCalendar, calendar['calendar'], schedule, newSchedule)
		newSchedule.calendar = monthCalendar
		newSchedule.schedule = json.dumps(schedule)

	
	# serialize month calendar
	def serialize_calendar(self,calendar):
		# convert all datetime object of calendar to string to serialize
		serialized_calendar = copy.deepcopy(calendar)
		for week in range(0, len(serialized_calendar)):
			for i in range(0, len(serialized_calendar[week])):
				serialized_calendar[week][i] = str(serialized_calendar[week][i])
		return json.dumps(serialized_calendar)


	# generate personal schedule of each worker
	def get_personal_schedule(self, year, month, calendarObj, calendar, schedule, newSchedule):
		# workers = MyUser.objects.filter(is_active=True).filter(has_working_schedule=True)
		for worker in newSchedule.users.all():
			personalSchedule = PersonalSchedule().personalSchedule(calendar, schedule, worker.username)
			PersonalWorkingSchedule.objects.create(user=worker, year=year, month=month, calendar=calendarObj, personalSchedule=json.dumps(personalSchedule))

	# validate all holidays
	def get_holidays(self):
		holidayList = []
		holidays = Holiday.objects.filter(noWorking=True)
		for holiday in holidays:
			if holiday.endDate < date.today():
				holiday.delete()
				pass
			d = holiday.startDate
			while d <= holiday.endDate:
				if d not in holidayList:
					holidayList.append(d)
				d += timedelta(days=1)
		return holidayList


	# # get list of workers working and their requests
	# get list of workers working and their requests
	def check_workers(self, newSchedule):
		# get all working workers and add them to schedule
		workers = MyUser.objects.filter(is_active=True).filter(has_working_schedule=True)
		employee = []
		for worker in workers:
			newSchedule.users.add(worker)
			# get each's default requests
			defaultRequest = PersonalDefaultWorkingRequest.objects.get(user=worker)
			default = []
			defa = [defaultRequest.sun_morning, defaultRequest.sun_evening, defaultRequest.mon, defaultRequest.tue,
			defaultRequest.wed, defaultRequest.thu, defaultRequest.fri, defaultRequest.sat]
			for i in range(0, len(defa)):
				if defa[i]:
					default.append(i)

			# get each's exceptional add days
			exceptionalAddDays = []
			exceptionAdds = ExceptionalWorkingDay.objects.filter(user=worker).filter(addDay=True)
			for exceptionAdd in exceptionAdds:
				if exceptionAdd.date < date.today():
					exceptionAdd.delete()
					pass
				exceptionalAddDays.append(exceptionAdd.date)

			# get each's exceptional cancel day
			exceptionalCancelDays = []
			exceptionCancels = ExceptionalWorkingDay.objects.filter(user=worker).filter(addDay=False)
			for exceptionCancel in exceptionCancels:
				if exceptionCancel.date < date.today():
					exceptionCancel.delete()
					pass
				exceptionalCancelDays.append(exceptionCancel.date)

			# append all to list and return
			employee.append(Employee(worker.username, default, exceptionalAddDays, exceptionalCancelDays))

		return employee




