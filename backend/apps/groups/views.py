from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from .models import GroupModel
from .serializers import GroupSerializer


class ListCreateGroupView(ListCreateAPIView):
    queryset = GroupModel.objects.all()
    serializer_class = GroupSerializer


class GetUpdateDeleteView(RetrieveUpdateDestroyAPIView):
    queryset = GroupModel.objects.all()
    serializer_class = GroupSerializer
