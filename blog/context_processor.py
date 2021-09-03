from .models import Category

def category_render(request):
    return {
        "all_categories": Category.objects.all()
    }