from rest_framework import serializers
from .models import *

#class for admin get/create holiday
class HolidaySerializer(serializers.ModelSerializer):
	class Meta:
		model = Holiday