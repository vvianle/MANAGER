import calendar
import math
import json
from datetime import datetime

# Create a list containing month calendar
class Calendar(object):

	def __init__(self, date):
		self.date = date

	def create_month_calendar(self):
		firstWeekday = calendar.monthrange(self.date.year, self.date.month)[0]
		monthDays = calendar.monthrange(self.date.year, self.date.month)[1]
		numWeeks = int(math.ceil((monthDays + firstWeekday+1)/7))

		monthCalendar = []
		for i in range(0, numWeeks):
			monthCalendar.append([])

		counter = 0
			
		# for the beginning of the month that does not work, append empty string
		for i in range (0, firstWeekday+1):
			monthCalendar[counter].append("")
		
		# for days that work, append date of day to mark
		for i in range(1, monthDays+1):
			monthCalendar[counter].append(str(i))
			# if it reaches Saturday, increment counter to enter new week
			if (int(self.day(self.date.month, i, self.date.year)) == 6):
				counter += 1

		while (len(monthCalendar[len(monthCalendar)-1]) < 7):
				monthCalendar[len(monthCalendar)-1].append("")

		return json.dumps(monthCalendar)

	# check what day of week a date falls on
	def day(self, M, D, Y):
		myDate = datetime.strptime(str(M)+'/'+str(D)+'/'+str(Y), '%m/%d/%Y')
		return int(datetime.date(myDate).strftime('%w'))

	