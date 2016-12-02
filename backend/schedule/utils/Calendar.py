from datetime import timedelta, date
from .Schedule import Schedule
import math
import copy

#Create a calendar
# given the string date, workers and their constraints and holidays
class Calendar(object):

	#initialize calendar with a date in type string
	def __init__(self, strDate, holidays, workers, newSchedule):
		self.date = strDate
		self.holiday = holidays
		self.workers = workers
		self.newSchedule = newSchedule
	
	# launch schedule and return according to request
	def launch(self):
		# convert the date
		month = self.date.month
		year = self.date.year
		day = self.date.day
		# get schedule
		return self.generateCalendar(day, month, year) 

	def generateCalendar(self, day, month, year):
		#days[i] = number of days in month i
		days = [0,31,28,31,30,31,30,31,31,30,31,30,31]

		#check for leap year
		if (year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0):
			days[2] = 29

		# calculate the number of shifts and weeks covered
		myDict = self.calculate(day, month, year, days[month])

		return self.getCalendar(year, month, days[month], myDict)
	

	# calculate the number of shifts and weeks covered to complete round
	def calculate(self, day, month, year, totalDayOfMonth):
		totalShift = 0
		d = copy.deepcopy(self.date)

		# calculate all total shift of that month from start date
		if len(self.workers) != 0:
			while d <= date(year, month, totalDayOfMonth):
				totalShift = self.update_total_shift(d, totalShift)
				d += timedelta(days=1)

		excessDay = 0
		if len(self.workers) != 0:
			# calculate total shift of excess day to make each workers work same number of shift
			while (totalShift % len(self.workers) != 0):
				excessDay += 1
				totalShift = self.update_total_shift(d, totalShift)
				d += timedelta(days=1)

		self.newSchedule.nextStartDate = d

		# calculate number of weeks covered and the average shift of each worker
		workingDays = totalDayOfMonth - day + 1
		numWeeks = int(math.ceil(float(workingDays + excessDay + int(self.date.strftime('%w')))/7))

		if len(self.workers) != 0:
			averageNumShifts = totalShift / len(self.workers)
		else:
			averageNumShifts = 0

		return {'numWeeks': numWeeks, 'numShifts': int(averageNumShifts), 'excessDay': excessDay}


	# update number of total shifts
	# check to see if it's a holiday -> no shift
	# sunday -> 2 shifts
	# otherwise, 1 shift
	def update_total_shift(self, d, totalShift):
		if d in self.holiday:
			return totalShift
		for worker in self.workers:
			if d in worker.exceptionalAddDays or (d not in worker.exceptionalCancelDays
				and int(d.strftime('%w'))+1 in worker.default):
				if int(d.strftime('%w')) == 0:
					totalShift += 2
				else:
					totalShift += 1
				break
		return totalShift


	# generate month working calendar as a list and return
	def getCalendar(self, year, month, totalDayOfMonth, myDict):
		calendar = []
		for i in range(0, myDict['numWeeks']):
			calendar.append([])
		counter = 0

		for i in range (0, int(self.date.strftime('%w'))):
			calendar[counter].append("")

		d = copy.deepcopy(self.date)
		
		while d <= date(year, month, totalDayOfMonth):
			calendar[counter].append(d)
			if int(d.strftime('%w')) == 6:
				counter += 1
			d += timedelta(days=1)

		for i in range(0, myDict['excessDay']):
			calendar[counter].append(d)
			if int(d.strftime('%w')) == 6:
				counter += 1
			d += timedelta(days=1)

		# append the not working days of last week with empty string
		while (len(calendar[len(calendar)-1]) < 7):
			calendar[len(calendar)-1].append("")

		return {'calendar': calendar, 'numShifts': myDict['numShifts']}


