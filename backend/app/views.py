from django.core.paginator import Paginator
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import View, ListView
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin

from backend.app.models import Post
from backend.app.forms import PostForm


class AllTwit(ListView):
    """Выводим все твиты"""
    model = Post
    queryset = Post.objects.all()
    context_object_name = 'posts'
    template_name = 'app/index.html'
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = PostForm()
        return context


class PostView(LoginRequiredMixin, View):
    """Сообщения пользователя"""
    def get(self, request):
        posts = Post.objects.filter(user=request.user)
        form = PostForm()
        paginator = Paginator(posts, 10)
        page = request.GET.get("page")
        page_obj = paginator.get_page(page)
        return render(request, "app/index.html", {"posts": posts,
                                                  "form": form,
                                                  "page_obj": page_obj})

    def post(self, request):
        form = PostForm(request.POST)
        if form.is_valid():
            pk = request.POST.get("id", None)
            form = form.save(commit=False)
            if pk is not None:
                form.parent = Post.objects.get(id=pk)
            form.user = request.user
            form.save()
            return redirect("home")
        else:
            return HttpResponse("error")


class Like(LoginRequiredMixin, View):
    """Ставим лайк"""
    def post(self, request):
        pk = request.POST.get("pk")
        post = Post.objects.get(id=pk)
        if request.user in post.user_like.all():
            post.user_like.remove(User.objects.get(id=request.user.id))
            post.like -= 1
        else:
            post.user_like.add(User.objects.get(id=request.user.id))
            post.like += 1
        post.save()
        return HttpResponse(status=201)


class PostsIFollow(LoginRequiredMixin, AllTwit):
    """Вывод твитов пользователя и его подписчиков"""
    model = Post
    template_name = 'app/index.html'
    context_object_name = 'posts'
    paginate_by = 10

    def get_queryset(self):
        qs = Post.objects.filter(
            Q(user_id__in=self.request.user.profile.get_followers) |
            Q(user_id=self.request.user.id)
        )
        return qs
