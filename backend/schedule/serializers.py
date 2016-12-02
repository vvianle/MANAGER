from rest_framework import serializers
from .models import *
from accounts.serializers import OneAuthenticatedUserSerializer

# class for user/admin to update default working constraints
class WorkingDefaultSerializer(serializers.ModelSerializer):
	user = OneAuthenticatedUserSerializer(read_only=True)
	class Meta:
		model = PersonalDefaultWorkingRequest

# class for user/admin to add/delete exceptional add/cancel working day.
class WorkingExceptionalDaySerializer(serializers.ModelSerializer):
	user = serializers.CharField(source='user.username', read_only=True)
	addDay = serializers.BooleanField(read_only=True)
	
	class Meta:
		model = ExceptionalWorkingDay

# class to serialize monthly working calendar
class WorkingCalendarSerializer(serializers.ModelSerializer):
	class Meta:
		model = WorkingCalendar
		fields = ('calendar',)

# class for user/admin to get working schedule and admin to post/update working schedule
class WorkingScheduleSerializer(serializers.ModelSerializer):
	users = serializers.StringRelatedField(many=True, read_only=True)
	calendar = WorkingCalendarSerializer(read_only=True)
	startDate = serializers.DateField(read_only=True)
	nextStartDate = serializers.DateField(read_only=True)

	class Meta:
		model = MonthlyWorkingSchedule

# class for user/admin to update personal default working constraints
class PersonalWorkingScheduleSerializer(serializers.ModelSerializer):
	user = OneAuthenticatedUserSerializer(read_only=True)
	calendar = WorkingCalendarSerializer(read_only=True)
	class Meta:
		model = PersonalWorkingSchedule



