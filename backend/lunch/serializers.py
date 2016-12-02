from rest_framework import serializers
from .models import *
from accounts.serializers import OneAuthenticatedUserSerializer

# class for user/admin update default lunch request
class LunchDefaultSerializer(serializers.ModelSerializer):
	user = OneAuthenticatedUserSerializer(read_only=True)
	class Meta:
		model = PersonalDefaultLunchSchedule

# class for user/admin create/delete exceptional add/cancel day
class LunchExceptionalDaySerializer(serializers.ModelSerializer):
	user = serializers.CharField(source='user.username', read_only=True)
	addDay = serializers.BooleanField(read_only=True)
	
	class Meta:
		model = ExceptionalLunchDay


# class for serializing month calendar
class MonthCalendarSerializer(serializers.ModelSerializer):
	class Meta:
		model = MonthCalendar
		fields = ('calendar',)

# class for user/admin see daily lunch request, admin to post new daily lunch request
class LunchRequestSerializer(serializers.ModelSerializer):
	users = OneAuthenticatedUserSerializer(many=True, read_only=True)
	calendar = MonthCalendarSerializer(read_only=True)
	class Meta:
		model = DailyLunchRequest

# class for user/admin to see personal monthly lunch summary
class PersonalMonthlyLunchSerializer(serializers.ModelSerializer):
	user = OneAuthenticatedUserSerializer(read_only=True)
	calendar = MonthCalendarSerializer(read_only=True)
	class Meta:
		model = PersonalMonthlyLunchOrder

# class for admin to see/create new meal price
class MealPriceSerializer(serializers.ModelSerializer):
	inUse = serializers.BooleanField(read_only=True)
	class Meta:
		model = MealPrice