from django.urls import path
from .views import *

urlpatterns = [
    path('', AllTwit.as_view(), name="home"),
    path('my/', PostView.as_view(), name="posts"),
    path('like/', Like.as_view()),
    path('favorites/', PostsIFollow.as_view(), name='favorites'),
]