from django.urls import path, re_path

from .views import *

urlpatterns = [
    path('', account, name='account'),
    path('settings/<int:userid>/', settings),
    re_path(r'^archive/(?P<year>[0-9]{4})/', archive),
]