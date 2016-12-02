from django.conf.urls import url
from .views import *

urlpatterns = [
	url(r'^default/(?P<pk>\d+)/$', LunchDefaultView.as_view(), name='lunch_default_view'),
	url(r'^add/(?P<pk>\d+)/$', LunchAddDayView.as_view(), name='lunch_add_view'),
	url(r'^cancel/(?P<pk>\d+)/$', LunchCancelDayView.as_view(), name='lunch_cancel_view'),
	url(r'^exceptional/(?P<pk>\d+)/(?P<date>\d{4}-\d{1,2}-\d{1,2})/$', LunchSingleExceptionalDayView.as_view(), name='single_lunch_exceptional_view'),
	
	url(r'^day/(?P<date>\d{4}-\d{1,2}-\d{1,2})/$', DailyLunchRequestView.as_view(), name='daily_lunch_request_view'),
	url(r'^day/current/$', CurrentLunchRequestView.as_view(), name='current_lunch_request_view'),
	
	url(r'^month/(?P<year>\d{4})/(?P<month>\d{1,2})/$', MonthlyLunchListView.as_view(), name='monthly_lunch_list_view'),
	url(r'^month/current/$', CurrentMonthlyLunchListView.as_view(), name='current_monthly_lunch_list_view'),
	
	url(r'^personal/(?P<pk>\d+)/(?P<year>\d{4})/(?P<month>\d{1,2})/$', PersonalMonthlyLunchView.as_view(), name='personal_monthly_lunch_view'),
	url(r'^personal/current/(?P<pk>\d+)/$', PersonalCurrentMonthlyLunchView.as_view(), name='personal_current_monthly_lunch_view'),
	
	url(r'^mealprice/$', MealPriceView.as_view(), name='meal_price_view'),
	url(r'^mealprice/(?P<startDate>\d{4}-\d{1,2}-\d{1,2})/$', SingleMealPriceView.as_view(), name='meal_price_view'),

	url(r'^request/$', EverydayLunchView.as_view(), name='everyday_lunch_view'),
]