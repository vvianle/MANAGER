# -*- coding: utf-8 -*-
from rest_framework import filters
from rest_framework import status
from rest_framework import generics
from rest_framework.renderers import JSONRenderer
from one_auth.authentication import OneTokenAuthentication
from .models import MyUser
from .permissions import IsAdminOrReadOnly, IsOneUserAuthenticated, IsOneSuperAdmin, IsOneSuperAdminOrIsSelf
from .serializers import OneUserSerializer, OneUserDetailsSerializer
from .serializers import OneAuthenticatedUserSerializer, ChangePasswordUserSerializer
from Calendar.views import JSONResponse


#GET /members/
#POST /members/
class AllUserList(generics.ListCreateAPIView):
    serializer_class = OneUserSerializer
    authentication_classes = (OneTokenAuthentication,)
    permission_classes = (IsAdminOrReadOnly,)
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = ('username', 'is_active', 'is_admin', 'has_working_schedule')

    def get_queryset(self):
        queryset = MyUser.objects.all()
        filt = self.request.GET.get('filter', None)
        print (filt)
        if filt is None:
            return queryset
        elif filt == 'working':
            return MyUser.objects.filter(is_active=True).filter(has_working_schedule=True)
        elif filt == 'lunch':
            return MyUser.objects.filter(is_active=True)


# GET /members/profile/
# PUT /members/profile/
# DELETE /members/profile/
class OneUserDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = MyUser.objects.all()
    serializer_class = OneUserDetailsSerializer
    authentication_classes = (OneTokenAuthentication,)
    permission_classes = (IsOneSuperAdmin,)
    renderer_classes = (JSONRenderer,)

    def get_object(self):
        return MyUser.objects.get(pk=self.kwargs['pk'])

    def perform_update(self, serializer):
        # Update password
        user = self.get_object()
        serializer.save()
        if "password" in self.request.data and self.request.data["password"] != "":
            password_serializer = ChangePasswordUserSerializer(data={"password": self.request.data["password"]})
            if password_serializer.is_valid(raise_exception=True):
                user.set_password(self.request.data["password"])
                user.save()
                # Logout all sessions if new password is not current password
                OneTokenAuthentication().delete_another_tokens(user)
                

    def perform_destroy(self, instance):
        # instance.delete()
        instance.is_active = 0
        instance.save()


# GET /members/profile/
# PUT /members/profile/
class OneAuthenticatedUserDetail(generics.RetrieveUpdateAPIView):
    queryset = MyUser.objects.all()
    serializer_class = OneUserDetailsSerializer
    authentication_classes = (OneTokenAuthentication,)
    permission_classes = (IsOneUserAuthenticated,)
    renderer_classes = (JSONRenderer,)

    def get_object(self):
        return self.request.user


# POST /members/profile/reset_password/
class OneUserSetPassword(generics.CreateAPIView):
    queryset = MyUser.objects.all()
    serializer_class = ChangePasswordUserSerializer
    authentication_classes = (OneTokenAuthentication,)
    permission_classes = (IsOneUserAuthenticated,)
    renderer_classes = (JSONRenderer,)

    def create(self, request, *args, **kwargs):
        user = request.user
        request_data = request.data
        print (request_data)
        if user.check_password(request_data["current_password"]):
            serializer = ChangePasswordUserSerializer(data={"password": self.request.data["new_password"]})
            if serializer.is_valid(raise_exception=True):
                if "new_password" in request_data:
                    user.set_password(request_data["new_password"])
                    user.save()
                    # Logout all sessions
                    if request_data["new_password"] != request_data["current_password"]:
                        OneTokenAuthentication().delete_another_tokens(user)
                    return JSONResponse({'status': 'success'}, status=status.HTTP_200_OK)
        else:
            return JSONResponse({'status': "fail",
                                 'data': {"password": "Current password is not correct"}},
                                status=status.HTTP_400_BAD_REQUEST)
