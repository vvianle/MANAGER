from django.conf.urls import url
from .views import *

urlpatterns = [
	url(r'^$', HolidayListView.as_view(), name='holiday_list_view'),
	url(r'^(?P<pk>\d+)/$', HolidayView.as_view(), name='holiday_view'),
]