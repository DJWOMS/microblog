from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import View
from backend.app.models import Post
from backend.app.forms import PostForm


class PostView(View):
    """"Сообщения пользователя"""
    def get(self, request):
        posts = Post.objects.filter(twit__isnull=True)
        form = PostForm()
        return render(request, "app/index.html", {"posts": posts, "form": form})

    def post(self, request):
        form = PostForm(request.POST)
        if form.is_valid():
            pk = request.POST.get("id", None)
            form = form.save(commit=False)
            if pk is not None:
                form.twit = Post.objects.get(id=pk)
            form.user = request.user
            form.save()
            return redirect("/")
        else:
            return HttpResponse("error")
