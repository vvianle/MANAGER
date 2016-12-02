from datetime import date
from accounts.models import MyUser
from holidays.models import Holiday
from lunch.models import *
from .Calendar import Calendar

class LunchOrder(object):

	def create_daily_lunch_list(self,lunchRequest, today):

		# delete all passed exceptional days
		self.validate_exceptional_days()

		# Create month calendar if it does not exist
		if not MonthCalendar.objects.filter(month=today.month).filter(year=today.year).exists():
			lunchRequest.calendar = MonthCalendar.objects.create(month=today.month, year=today.year, calendar=Calendar(today).create_month_calendar())
		else:
			lunchRequest.calendar = MonthCalendar.objects.filter(month=today.month).get(year=today.year)

		# validate meal price and set meal price for that dat
		self.update_meal_price(today)
		lunchRequest.price = MealPrice.objects.get(inUse=True).price

		self.check_members_request(lunchRequest,today)


	def isHoliday(self, today):
		holidays = Holiday.objects.filter(noLunch=True)
		for holiday in holidays:
			if holiday.endDate < today:
				holiday.delete()
				pass
			if holiday.startDate <= today and today <= holiday.endDate:
				return True
		return False


	# delete all passed exceptional days
	def validate_exceptional_days(self):
		exceptionalDays = ExceptionalLunchDay.objects.all()
		for exceptionalDay in exceptionalDays:
			if exceptionalDay.date < date.today():
				exceptionalDay.delete()

	
	# check member request to see if they request meal that day
	def check_members_request(self, lunchRequest, today):
		members = MyUser.objects.filter(is_active=True)
		for member in members:
			defaultRequest = PersonalDefaultLunchSchedule.objects.get(user=member)
			default = [defaultRequest.mon, defaultRequest.tue, defaultRequest.wed, defaultRequest.thu, defaultRequest.fri]
			# if it's an exceptional cancel day, don't register
			if ExceptionalLunchDay.objects.filter(user=member).filter(date=today).filter(addDay=False).exists():
				pass
			# elif it's an exceptional add day or a default request day, register a meal
			# create/update personal monthly lunch summary
			elif (default[int(today.strftime('%w'))-1] or 
				ExceptionalLunchDay.objects.filter(user=member).filter(date=today).filter(addDay=True).exists()):
				lunchRequest.users.add(member)
				lunchRequest.totalOrders += 1
				monthCalendar = MonthCalendar.objects.get(year=today.year, month=today.month)
				monthlyLunchOrder, created = PersonalMonthlyLunchOrder.objects.get_or_create(user=member, 
					month=today.month, year=today.year, calendar=monthCalendar)
				self.update_personal_monthly_lunch_orders(monthlyLunchOrder, today, lunchRequest.price)
				

	# validate meal price
	# delete all passed unUsed meal price
	def update_meal_price(self, today):
		nextMealPrices = MealPrice.objects.filter(inUse=False)
		for nextMealPrice in nextMealPrices:
			if nextMealPrice.startDate == today:
				if MealPrice.objects.filter(inUse=True).exists():
					MealPrice.objects.get(inUse=True).delete()
				nextMealPrice.inUse = True
				nextMealPrice.save()
				return
			elif nextMealPrice.startDate < today:
				nextMealPrice.delete()
		# else make a default meal price
		if not MealPrice.objects.filter(inUse=True).exists():
			MealPrice.objects.create(inUse=True)

	# update each person's monthly lunch summary
	def update_personal_monthly_lunch_orders(self, monthlyLunchOrder, date, price):
		if not monthlyLunchOrder.orderDays:
			monthlyLunchOrder.orderDays = str(date.day)
		else:
			monthlyLunchOrder.orderDays = str(monthlyLunchOrder.orderDays) + ',' + str(date.day)
		monthlyLunchOrder.totalPrice += (1*price)
		monthlyLunchOrder.numMeal += 1
		monthlyLunchOrder.save()