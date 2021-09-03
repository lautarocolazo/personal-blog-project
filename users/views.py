from django.shortcuts import render, redirect, get_object_or_404
from . import views
from blog.models import Profile
from django.views import generic
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.views.generic import DetailView, CreateView
from django.urls import reverse_lazy
from django.contrib.auth.views import PasswordChangeView
from .forms import SignUpForm, EditProfileForm, PasswordChangingForm, ProfilePageForm

# Create your views here.
class CreateProfileView(generic.CreateView):
    model = Profile
    form_class = ProfilePageForm
    template_name = "registration/create_profile_page.html"
    # fields = '__all__'
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class EditProfilePageView(generic.UpdateView):
    model = Profile
    template_name = "registration/edit_profile_page.html"
    fields = ['bio', 'pic', 'fb_url', 'tw_url', 'ig_url' ]
    success_url = reverse_lazy('home')


class ShowProfileView(generic.DetailView):
    model = Profile
    template_name = "registration/user_profile.html"

    def get_context_data(self, *args, **kwargs):
        # users = Profile.objects.all()
        context = super(ShowProfileView, self).get_context_data(*args, **kwargs)

        page_user = get_object_or_404(Profile, id=self.kwargs["pk"])

        context["page_user"] = page_user
        return context

class PasswordsChangeView(PasswordChangeView):
    form_class = PasswordChangingForm
    success_url = reverse_lazy('password_success')

def password_success(request):
    return render(request, "registration/password_success.html")

class UserRegisterView(generic.CreateView):
    form_class = SignUpForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')

class UserEditView(generic.UpdateView):
    form_class = EditProfileForm
    template_name = 'registration/edit_profile.html'
    success_url = reverse_lazy('home')

    def get_object(self):
        return self.request.user



