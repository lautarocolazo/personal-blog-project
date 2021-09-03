from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth.models import User
from blog.models import Profile

class ProfilePageForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('bio', 'pic', 'fb_url', 'tw_url', 'ig_url')
        widgets = {
                'bio': forms.Textarea(attrs={'class': 'field'}),
                'pic': forms.ClearableFileInput(),
                'fb_url': forms.TextInput(attrs={'class': 'field'}),
                'tw_url': forms.TextInput(attrs={'class': 'field'}),
                'ig_url': forms.TextInput(attrs={'class': 'field'}),
        }

class SignUpForm(UserCreationForm):
    email = forms.EmailField()
    first_name = forms.CharField(max_length=64)
    last_name = forms.CharField(max_length=64)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

class EditProfileForm(UserChangeForm):
    email = forms.EmailField()
    first_name = forms.CharField(max_length=64)
    last_name = forms.CharField(max_length=64)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')

class PasswordChangingForm(PasswordChangeForm):
    old_password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'field'}))
    new_password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'field'}))
    new_password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'field'}))

    class Meta:
        model = User
        fields = ('old_password', 'new_password1', 'new_password2')