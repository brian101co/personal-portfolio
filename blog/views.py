from django.shortcuts import render, get_object_or_404
from django.views import View
from .models import Post

class BlogListView(View):
    def get(self, request):
        posts = Post.published.all()
        return render(request, 'blog/blog_list.html', {'posts':posts})

class BlogDetailView(View):
    def get(self, request, slug):
        post = get_object_or_404(Post, slug=slug)
        return render(request, 'blog/blog_detail.html', {'post':post})
