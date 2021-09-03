from django.shortcuts import render, get_object_or_404
from .models import Post, Category, Comment
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .forms import PostForm, EditForm, CommentForm
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect
# Create your views here.


# def home(request):
#     posts = Post.objects.all()
#     return render(request, "blog/home.html",{
#         "posts": posts
#     })
def LikeView(request, post_id):
    post = get_object_or_404(Post, id=request.POST.get("post_id")) 
    liked = False
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        liked = False
    else:
        post.likes.add(request.user)
        liked = True
    return HttpResponseRedirect(reverse("article", args=[str(post_id)]))



def CategoryView(request, cats):
    posts = Post.objects.all()
    category_post = Post.objects.filter(category=cats.title().replace("-", " "))
    return render(request, "blog/category.html", {
        "category_post": category_post, "cats": cats
    })

class HomeView(ListView):
    model = Post
    template_name = 'blog/home.html'
    ordering = ['-created']

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(HomeView, self).get_context_data(*args, **kwargs)
        context["cat_menu"] = cat_menu
        return context

class ArticleDetailView(DetailView):
    model = Post
    template_name = 'blog/article_detail.html'

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(ArticleDetailView, self).get_context_data(*args, **kwargs)

        stuff = get_object_or_404(Post, id=self.kwargs['pk'])
        total_likes = stuff.total_likes()

        liked = False
        if stuff.likes.filter(id=self.request.user.id).exists():
            liked = True

        context["cat_menu"] = cat_menu
        context["total_likes"] = total_likes
        context["liked"] = liked
        return context

class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/add_post.html'
    # fields = '__all__'

class AddCommentView(CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'blog/add_comment.html'
    # fields = '__all__'

    def form_valid(self, form):
        form.instance.post_id = self.kwargs['pk'] 
        return super().form_valid(form)

    success_url = reverse_lazy('home')

class AddCategoryView(CreateView):
    model = Category
    # form_class = PostForm
    template_name = 'blog/add_category.html'
    fields = '__all__'

class UpdatePostView(UpdateView):
    model = Post
    form_class = EditForm
    template_name = 'blog/update_post.html'

class DeletePostView(DeleteView):
    model = Post
    template_name = 'blog/delete_post.html'
    success_url = reverse_lazy('home')

def about(request):
    return render(request, "blog/about.html")

    