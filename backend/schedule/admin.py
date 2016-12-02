from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(MonthlyWorkingSchedule)
admin.site.register(ExceptionalWorkingDay)
admin.site.register(PersonalDefaultWorkingRequest)
admin.site.register(PersonalWorkingSchedule)
admin.site.register(WorkingCalendar)