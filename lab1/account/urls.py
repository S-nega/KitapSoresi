from django.urls import path, re_path

from .views import *

urlpatterns = [
    path('', account, name='account'),
    path('settingsPage/<int:userid>/', settingsPage),
    re_path(r'^archive/(?P<year>[0-9]{4})/', archive),
]