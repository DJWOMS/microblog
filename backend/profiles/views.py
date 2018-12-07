from django.shortcuts import render,get_object_or_404,redirect
from .models import Profile
from .forms import ProfileForm
from django.views import View
from django.views.generic import UpdateView,DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.contrib import messages

class ProfileView(LoginRequiredMixin,DetailView):
    model = Profile
    context_object_name = 'profile'
    template_name = 'profiles/profile_detail.html'

    def get_object(self,queryset=None):
        obj = get_object_or_404 (
            Profile,
            user = self.request.user
        )
        if obj.user != self.request.user:
            raise Http404
        return obj

class ProfileEditView(LoginRequiredMixin,UpdateView):
    form_class = ProfileForm
    model = Profile
    template_name = 'profiles/profile_edit.html'
    success_url = reverse_lazy('view_profile')

    def get_object(self,queryset=None):
        return self.request.user.profile

    def form_valid(self,form):
        messages.success(self.request,'Profile has been updated!')
        return super().form_valid(form)
