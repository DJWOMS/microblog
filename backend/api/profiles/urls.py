from django.urls import path
from .views import *

urlpatterns = [
    path('', ProfileUser.as_view()),
    path('public-info/', PublicUserInfo.as_view()),
    path('update-ava/', UpdateProfile.as_view()),
    path('update-nike/', UpdateNike.as_view()),
    path('follow/', AddFollow.as_view()),
]