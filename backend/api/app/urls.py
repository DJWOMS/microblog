from django.urls import path
from .views import *

urlpatterns = [
    path('', TweetsAll.as_view()),
    path('my/', UserTweet.as_view()),
    path('like/', Like.as_view()),
    path('favorites/', PostIFollow.as_view()),
]