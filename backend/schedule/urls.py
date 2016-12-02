from django.conf.urls import url
from .views import *

urlpatterns = [
	url(r'^default/(?P<pk>\d+)/$', WorkingDefaultView.as_view(), name='working_default_view'),
	url(r'^add/(?P<pk>\d+)/$', WorkingAddDayView.as_view(), name='working_add_view'),
	url(r'^cancel/(?P<pk>\d+)/$', WorkingCancelDayView.as_view(), name='working_cancel_view'),
	url(r'^exceptional/(?P<pk>\d+)/(?P<date>\d{4}-\d{1,2}-\d{1,2})/$', WorkingSingleExceptionalDayView.as_view(), name='single_working_exceptional_view'),

	url(r'^schedule/(?P<year>\d{4})/(?P<month>\d{1,2})/$', WorkingScheduleView.as_view(), name='working_schedule_view'),
	url(r'^schedule/current/$', CurrentWorkingScheduleView.as_view(), name='current_working_schedule_view'),
	
	url(r'^personal/(?P<pk>\d+)/(?P<year>\d{4})/(?P<month>\d{1,2})/$', PersonalWorkingScheduleView.as_view(), name='personal_working_schedule_view'),
	url(r'^personal/current/(?P<pk>\d+)/$', PersonalCurrentWorkingScheduleView.as_view(), name='personal_current_working_schedule_view'),
	
	url(r'^generate/$', GenerateScheduleView.as_view(), name='generate_schedule_view'),
]