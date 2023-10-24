
from django.urls import path, include

urlpatterns = [
    path('groups', include('apps.groups.urls')),
    path('users', include('apps.users.urls')),
]
