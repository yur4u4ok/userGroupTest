from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from apps.users.serializers import UserSerializer

from .models import UserModel


class ListCreateUsersView(ListCreateAPIView):
    queryset = UserModel.objects.all()
    serializer_class = UserSerializer


class GetUpdateDeleteUser(RetrieveUpdateDestroyAPIView):
    queryset = UserModel.objects.all()
    serializer_class = UserSerializer
