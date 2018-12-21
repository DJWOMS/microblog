from django.urls import path
from .views import *

urlpatterns = [
    path('', ProfileUser.as_view()),
    path('public-info/', PublicUserInfo.as_view()),
]