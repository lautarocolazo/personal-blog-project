from django import forms
from .models import Post, Category, Comment

choices = Category.objects.all().values_list('name', 'name')

choice_list = []

for choice in choices:
    choice_list.append(choice)

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'title_tag', 'author', 'category', 'image', 'snippet', 'body')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'field'}),
            'title_tag': forms.TextInput(attrs={'class': 'field'}),
            'author': forms.Select(attrs={'class': 'field'}),
            'category': forms.Select(choices=choice_list, attrs={'class': 'field'}),
            'image': forms.ClearableFileInput(),
            'body': forms.Textarea(attrs={'class': 'field'}),
            'snippet': forms.Textarea(attrs={'class': 'field'})
        }

class EditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'title_tag', 'category', 'image', 'snippet', 'body')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'field'}),
            'title_tag': forms.TextInput(attrs={'class': 'field'}),
            # 'author': forms.Select(attrs={'class': 'field'}),
            'category': forms.Select(choices=choice_list, attrs={'class': 'field'}),
            'image': forms.ClearableFileInput(),
            'body': forms.Textarea(attrs={'class': 'field'}),
            'snippet': forms.Textarea(attrs={'class': 'field'}),

        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'body')

        widgets = {
            'name': forms.TextInput(attrs={'class': 'field'}),
            'body': forms.Textarea(attrs={'class': 'field'}),
        }