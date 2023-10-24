from django.urls import path

from .views import ListCreateGroupView, GetUpdateDeleteView

urlpatterns = [
    path('', ListCreateGroupView.as_view(), name='list_create_groups'),
    path('/<int:pk>', GetUpdateDeleteView.as_view(), name='get_update_delete_group'),
]