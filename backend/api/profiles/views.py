from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework import permissions
from rest_framework.response import Response

from backend.app.models import Post
# from backend.api.app.serializers import PostSerializer
from backend.profiles.models import Profile
from .serializers import ProfileSer, PostSerializer, EditAvatar, EditNike


class ProfileUser(APIView):
    """Вывод профиля пользователя"""
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        ser = ProfileSer(Profile.objects.get(user=request.user))
        return Response(ser.data)


class PublicUserInfo(APIView):
    """Публичный профиль пользователя"""
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        obj = Post.objects.filter(user__profile__id=request.GET.get('pk'))
        ser = PostSerializer(obj, many=True)
        return Response(ser.data)


class UpdateProfile(APIView):
    """Редактирование профиля"""
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        prof = Profile.objects.get(user=request.user)
        ser = EditAvatar(prof, data=request.data)
        if ser.is_valid():
            if "avatar" in request.FILES:
                ser.save(avatar=request.FILES["avatar"])
                return Response(status=201)
        else:
            return Response(status=400)


class UpdateNike(APIView):
    """Редактирование профиля"""
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        prof = Profile.objects.get(user=request.user)
        ser = EditNike(prof, data=request.data)
        if ser.is_valid():
            ser.save()
            return Response(status=201)
        else:
            return Response(status=400)

