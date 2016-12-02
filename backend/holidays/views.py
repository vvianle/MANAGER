from rest_framework import generics
from .models import *
from .serializers import *
from accounts.permissions import *
from one_auth.authentication import OneTokenAuthentication

# GET /holidays/
# POST /holidays/
class HolidayListView(generics.ListCreateAPIView):
	queryset = Holiday.objects.all()
	serializer_class = HolidaySerializer
	authentication_classes = (OneTokenAuthentication,)
	permission_classes = (IsAdminOrReadOnly, )

# GET /holidays/(?P<pk>\d+)/
# DELETE /holidays/(?P<pk>\d+)/
class HolidayView(generics.RetrieveDestroyAPIView):
	serializer_class = HolidaySerializer
	permission_classes = (IsAdminOrReadOnly, )
	authentication_classes = (OneTokenAuthentication,)
	lookup_field = ('pk')
	queryset = Holiday.objects.all()