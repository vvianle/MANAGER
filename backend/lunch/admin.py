from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(ExceptionalLunchDay)
admin.site.register(DailyLunchRequest)
admin.site.register(PersonalDefaultLunchSchedule)
admin.site.register(PersonalMonthlyLunchOrder)
admin.site.register(MealPrice)
admin.site.register(MonthCalendar)