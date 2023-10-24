from django.urls import path

from .views import ListCreateUsersView, GetUpdateDeleteUser

urlpatterns = [
    path('', ListCreateUsersView.as_view(), name='list_create_users'),
    path('/<int:pk>', GetUpdateDeleteUser.as_view(), name='get_update_delete_user'),
]
