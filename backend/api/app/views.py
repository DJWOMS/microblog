from rest_framework.views import APIView
from rest_framework import permissions
from rest_framework.response import Response
from backend.app.models import Post
from backend.api.app.serializers import PostSerializer


class TweetsAll(APIView):
    """Вывод всех твитов"""
    permission_classes = [permissions.AllowAny]

    def get(self, request):
        tweets = Post.objects.all()
        ser = PostSerializer(tweets, many=True)
        return Response(ser.data)
