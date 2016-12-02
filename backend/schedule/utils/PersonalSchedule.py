# generate personal schedule of a worker
class PersonalSchedule(object):

	# get personal schedule
	def personalSchedule(self, calendar, myWeekList, name):

		personalSchedule = []

		# iterate through the working schedule, if name of worker appears,
		# add day to his personal schedule
		for x in range(0, len(myWeekList)):
			for i in range(0, len(myWeekList[x])):
				if name == myWeekList[x][i]:
					personalSchedule.append(str(calendar[x][i]))
				# distinguish Sunday morning/evening shift
				elif str(myWeekList[x][i]) == (name+' | '+name):
					personalSchedule.append(str(calendar[x][i])+' Morning')
					personalSchedule.append(str(calendar[x][i])+' Evening')
				elif str(myWeekList[x][i]).startswith(name + ' | '):
					personalSchedule.append(str(calendar[x][i])+' Morning')
				elif str(myWeekList[x][i]).endswith(' | ' + name):
					personalSchedule.append(str(calendar[x][i])+' Evening')

		return personalSchedule