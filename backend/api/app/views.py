from django.contrib.auth.models import User
from django.db.models import Q
from rest_framework.views import APIView
from rest_framework import permissions
from rest_framework.response import Response
from backend.app.models import Post
from backend.api.app.serializers import PostSerializer, AddTweetSerializer


class TweetsAll(APIView):
    """Вывод всех твитов"""
    permission_classes = [permissions.AllowAny]

    def get(self, request):
        tweets = Post.objects.all()
        ser = PostSerializer(tweets, many=True)
        return Response(ser.data)


class UserTweet(APIView):
    """Твиты пользователя"""
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        tweets = Post.objects.filter(user=request.user)
        ser = PostSerializer(tweets, many=True)
        return Response(ser.data)

    def post(self, request):
        ser = AddTweetSerializer(data=request.data)
        print(request.data.get("id"))
        if ser.is_valid():
            if request.data.get("id"):
                ser.save(parent_id=request.data.get("id"), user=request.user)
            else:
                ser.save(user=request.user)
            return Response(status=200)
        else:
            return Response(status=400)


class PostIFollow(APIView):
    """Твиты пользователя и его посдписчиков"""
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        qs = Post.objects.filter(
            Q(user_id__in=request.user.profile.get_followers) |
            Q(user_id=request.user.id)
        )
        ser = PostSerializer(qs, many=True)
        return Response(ser.data)


class Like(APIView):
    """Ставим лайк"""
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        pk = request.data.get("pk")
        post = Post.objects.get(id=pk)
        if request.user in post.user_like.all():
            post.user_like.remove(User.objects.get(id=request.user.id))
            post.like -= 1
        else:
            post.user_like.add(User.objects.get(id=request.user.id))
            post.like += 1
        post.save()
        return Response(status=201)


