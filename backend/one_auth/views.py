from datetime import datetime
from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.parsers import JSONParser
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from one_auth.models import OneAuthToken
from one_auth.authentication import OneTokenAuthentication
from one_auth.serializers import OneLoginSerializer
from accounts.permissions import IsOneUserAuthenticated
from Calendar.views import JSONResponse


class LoginView(GenericAPIView):
    permission_classes = (AllowAny,)
    serializer_class = OneLoginSerializer

    def post(self, request, format=None):
        data = JSONParser().parse(request)
        self.serializer = self.get_serializer(data=data)
        self.serializer.is_valid(raise_exception=True)
        self.user = self.serializer.validated_data['user']
        if self.user:
            token = OneAuthToken.objects.create(user=self.user)
            self.user.last_login = datetime.now()
            self.user.save()
            return JSONResponse({"token": token}, status=status.HTTP_200_OK)


class LogoutView(APIView):
    authentication_classes = (OneTokenAuthentication,)
    permission_classes = (IsOneUserAuthenticated,)

    def post(self, request, format=None):
        request._auth.delete()
        return JSONResponse({"sucess": "true"}, status=status.HTTP_200_OK)
