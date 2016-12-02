import copy
import datetime

# create a schedule
class Schedule(object):

	def __init__(self, calendar, workers, holiday, startDate, numShifts):
		self.calendar = calendar
		self.workers = workers
		self.holiday = holiday
		self.startDate = startDate
		self.averageNumShifts = numShifts

	# generate working schedule for workers
	def launch(self):
		weekList = copy.deepcopy(self.calendar)
		self.setHoliday(weekList)

		if len(self.workers) != 0:
			# schedule the weekends first
			self.weekendSchedule(weekList)
			# then the week days  
			self.weekSchedule(weekList)
			# rearrange shift to make sure everyone works the same number of shifts
			self.arrangeShift(weekList)
		else:
			self.emptySchedule(weekList)
		return weekList


	# mark all holiday in schedule
	def setHoliday(self, weekList):
		for week in weekList:
			for i in range(0, len(week)):
				if type(week[i]) == datetime.date and week[i] in self.holiday:
						week[i] = 'Holiday'

	# if there is no worker working - set schedule to OPEN
	def emptySchedule(self, weekList):
		for week in weekList:
			for i in range(0, len(week)):
				if type(week[i]) == datetime.date:
					if i == 0:
						week[i] = 'OPEN | OPEN'
					else:
						week[i] = 'OPEN'

	# schedule the weekend 
	def weekendSchedule(self, weekList):
		# for each day of each week, if it's a working day
		for week in weekList:
			for i in range(0, len(week)):
				# if it's saturday
				if (i==6) and type(week[i]) == datetime.date:
					for person in self.workers:
						# if a person can work, assign that shift to them and move them to the end of list
						if week[i] in person.exceptionalAddDays or (week[i] not in 
							person.exceptionalCancelDays and 7 in person.default):
							week[i] = person.name
							person.counter += 1
							self.workers.insert(len(self.workers)-1, self.workers.pop(
								self.workers.index(person)))
							break
					else:
						week[i] = 'OPEN'
				# if it's sunday
				elif (i==0) and type(week[i])==datetime.date:
					for person in self.workers:
						# fill in sunday morning first
						# if a person can work, assign that shift to them and move them to the end of list
						if week[i] in person.exceptionalAddDays or (week[i] not in 
							person.exceptionalCancelDays and 0 in person.default):
							week[i] = person.name + ' | '
							person.counter += 1
							self.workers.insert(len(self.workers)-1, self.workers.pop(
								self.workers.index(person)))
							break
					else:
						week[i] = 'OPEN | '
					# fill in sunday evening
					# if a person can work, assign that shift to them and move them to the end of list
					for person in self.workers:
						if week[i] in person.exceptionalAddDays or (week[i] not in 
							person.exceptionalCancelDays and 1 in person.default):
							week[i] += person.name
							person.counter += 1
							self.workers.insert(len(self.workers)-1, self.workers.pop(
								self.workers.index(person)))
							break
					else:
						week[i] += week[i] + 'OPEN'



	#schedule week days
	def weekSchedule(self, weekList):
		for week in weekList:
			for person in self.workers:
				if person.name in week[0] or person.name in week[6]:
					self.workers.insert(len(self.workers)-1, self.workers.pop(
								self.workers.index(person)))
			for i in range(1, len(week)-1):
				canWorkThisDay = []
				work1DayApart = []
				work2DayApart = []
				# for each day of week, if it's a working day
				if type(week[i])==datetime.date:
					for person in self.workers:
						# if they can work, check if they have worked recently
						# if they did, check other people
						if week[i] in person.exceptionalAddDays or (week[i] not in 
							person.exceptionalCancelDays and (i+1) in person.default):
							canWorkThisDay.append(person)
							if (self.workedRecently(i, week, weekList, person) == 1):
								work1DayApart.append(person)
							elif (self.workedRecently(i, week, weekList, person) == 2):
								work2DayApart.append(person)
							else:
								# otherwise, assign shift to them and move them the end of list
								week[i] = person.name
								person.counter += 1
								self.workers.insert(len(self.workers)-1, self.workers.pop(
									self.workers.index(person)))
								break
					else:
						# switch shift with people who can work but worked recently
						if not self.switchShift(i, week, weekList, canWorkThisDay):
							if not self.secondBestOption(work1DayApart, work2DayApart, week, i):
								week[i] = 'OPEN'

	
	# check if they have worked recently
	# return 1 if they worked 1 day apart, 2 if 2 days apart or 0 if they haven't worked recently
	def workedRecently(self, i, week, weekList, person):
		# if it's Monday, check if it's in the first week or otherwise
		if (i==1):
			if week == weekList[0]:
				if (person.name in str(week[i-1])) or (person.name in str(week[i+1])):
					return 1
				elif (person.name in str(week[i+2])):
					return 2
			else:
				if (person.name in str(weekList[weekList.index(week)-1][6])) or (person.name in str(week[i+2])): 
					return 2
				elif (person.name in str(week[i-1])) or (person.name in str(week[i+1])):
					return 1
		# if it's Friday, check if it's in the last week or otherwise
		elif (i==5):
			if week == weekList[len(weekList)-1]:
				if (person.name in str(week[i-1])) or (person.name in str(week[i+1])):
					return 1
				elif (person.name in str(week[i-2])):
					return 2
			else:
				if (person.name in str(week[i-1])) or (person.name in str(week[i+1])):
					return 1
				elif (person.name in str(week[i-2])) or (person.name in str(weekList[weekList.index(week)+1][0])):
					return 2
		# otherwise, check normally
		else:
			if (person.name in str(week[i-1])) or (person.name in str(week[i+1])):
				return 1 
			elif (person.name in str(week[i-2])) or (person.name in str(week[i+2])):
				return 2
		return 0


	# switch shift with 2 previous closest shift
	def switchShift(self, i, week, weekList, canWorkThisDay):
		# return if it falls on first day of week or month
		if (weekList.index(week) == 0 and i == int(self.startDate.strftime('%w'))) or i == 1:
			return False
		# check switching for first previous closest day
		if self.checkShiftSwitch(i, week, weekList, canWorkThisDay, 1):
			return True
		if (weekList.index(week) == 0 and i == int(self.startDate.strftime('%w')) + 1) or i == 2:
			return False
		# check switching for second previous closest day
		return self.checkShiftSwitch(i, week, weekList, canWorkThisDay, 2)


	# see if can switch shift
	def checkShiftSwitch(self, i, week, weekList, canWorkThisDay, indexShift):
		objectChange = 0
		# check if person doing previous day can do the day switching
		for a in canWorkThisDay:
			if week[i-indexShift] == a.name:
				objectChange = a
		# if can, see if anyone can take his old shift
		if objectChange != 0:
			week[i-indexShift] = "0"
			for person in self.workers:
				# if they can switch, switch their shifts and update counter
				if (self.calendar[weekList.index(week)][i-indexShift] in person.exceptionalAddDays or (
					self.calendar[weekList.index(week)][i-indexShift] not in person.exceptionalCancelDays 
					and (i-indexShift+1) in person.default) and 
					self.workedRecently(i-indexShift, week, weekList, person) == 0 and
					self.workedRecently(i, week, weekList, objectChange) == 0):
					
					week[i-indexShift] = person.name
					person.counter += 1
					week[i] = objectChange.name
					self.workers.insert(len(self.workers)-1, self.workers.pop(
								self.workers.index(person)))
					return True
			# otherwise, resume state
			week[i-indexShift] = objectChange.name
			return False


	# secondbest option if no one can fill in the shifts
	def secondBestOption(self, work1DayApart, work2DayApart, week, i):
		# if there are people working 2 days apart, give them the shift
		if len(work2DayApart) != 0:
			week[i] = work2DayApart[0].name
			work2DayApart[0].counter += 1
			return True
			self.workers.insert(len(self.workers)-1, self.workers.pop(self.workers.index(work2DayApart[0])))
		# otherwise if there are people working 1 day apart, give them the shift
		elif len(work1DayApart) != 0:
			week[i] = work1DayApart[0].name
			work1DayApart[0].counter += 1
			self.workers.insert(len(self.workers)-1, self.workers.pop(self.workers.index(work1DayApart[0])))
			return True
		return False


	# rearrange shift to make sure everyone works the same number of shifts
	def arrangeShift(self, weekList):
		sameNumberShift = True
		# for each worker, if they work less than they suppose to
		# move them to start of list and stop to check first
		for person in self.workers:
			if person.counter < self.averageNumShifts:
				self.workers.insert(0, self.workers.pop(self.workers.index(person)))
				sameNumberShift = False
				break
		if not sameNumberShift:
			# see if arrange shift 2 days apart
			if not self.equalizeShift(weekList, 0):
				if not self.equalizeShift(weekList, 2):
					# see if arrange shift 1 day apart
					return self.equalizeShift(weekList, 1)
				return True
			return True
		return True

	
	# arrange shift so people do same amount of shifts
	def equalizeShift(self, weekList, myRange):
		# check the remaining workers
		for a in range(1, len(self.workers)):
			for week in weekList:
				# if there are 8 workers, try to make each of time work once a week
				if len(self.workers) >= 8 and (self.workers[0].name in week or self.workers[0].name in week[0]):
					pass
				else:
					for i in range(1, len(week)-1):         
						# to ensure weekends are equally divide, check the week days only
						# check the shift of remaining workers
						if self.workers[a].name in week[i]:
							if self.calendar[weekList.index(week)][i] in self.workers[0].exceptionalAddDays or (
								self.calendar[weekList.index(week)][i] not in self.workers[0].exceptionalCancelDays 
								and (i+1) in self.workers[0].default):
								# if he can, assign him to the shift,
								# change the workers' counter accordingly
								# move the first worker to last, call recursion to continue checking
								if self.workedRecently(i, week, weekList, self.workers[0]) == myRange:
									week[i] = week[i].replace(self.workers[a].name, self.workers[0].name)
									self.workers[0].counter += 1
									self.workers[a].counter -= 1
									self.workers.insert(len(self.workers)-1, self.workers.pop(0))
									if self.arrangeShift(weekList):
										return True
		return False
