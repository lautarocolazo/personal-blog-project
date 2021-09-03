from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from ckeditor.fields import RichTextField
# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500)
    pic = models.ImageField(upload_to="bios", blank=True, null=True)
    fb_url = models.CharField(max_length=255, null=True, blank=True)
    tw_url = models.CharField(max_length=255, null=True, blank=True)
    ig_url = models.CharField(max_length=255, null=True, blank=True)
  

    def __str__(self):
        return str(self.user)

    def get_absolute_url(self):
        # return reverse('article', args=(str(self.id)))
        return reverse('home')

class Category(models.Model):
    name = models.CharField(max_length=64)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        # return reverse('article', args=(str(self.id)))
        return reverse('home')

class Post(models.Model):
    title = models.CharField(max_length=255)
    title_tag = models.CharField(max_length=255, default="Tag for your post")
    author = models.ForeignKey(User, on_delete=models.CASCADE) 
    # body = models.TextField()
    body = RichTextField(blank=True, null=True)
    snippet = models.CharField(max_length=200, default="Here goes your post snippet")
    image = models.ImageField(upload_to="media", blank=True, null=True)
    category = models.CharField(max_length=64, default="Category")
    likes = models.ManyToManyField(User, related_name="blog_post")
    

    created = models.DateTimeField(auto_now_add=True)
    udpated = models.DateTimeField(auto_now_add=True)

    def total_likes(self):
        return self.likes.count()

    def __str__(self):
        return f"{self.title} | {self.author}"

    def get_absolute_url(self):
        # return reverse('article', args=(str(self.id)))
        return reverse('home')

class Comment(models.Model):
    post = models.ForeignKey(Post, related_name="comments", on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    body = models.TextField(max_length=500)

    created = models.DateTimeField(auto_now_add=True)
    udpated = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s - %s' % (self.post.title, self.name)



