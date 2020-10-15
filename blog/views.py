from django.shortcuts import render, get_object_or_404
from django.views import View
from .models import Post
from jobs.models import Job
from django.db.models import Count

class BlogListView(View):
    def get(self, request):
        posts = Post.published.posts()
        context = {
            'posts': posts,
        }
        return render(request, 'blog/blog_list.html', context=context)

class BlogDetailView(View):
    def get(self, request, slug):
        post = get_object_or_404(Post, slug=slug)
        post_tags_ids = post.tags.values_list('id', flat=True) #list of of tag IDs [1,3,7]
        similar_posts = Post.published.posts().filter(tags__in=post_tags_ids).exclude(id=post.id)
        similar_posts = similar_posts.annotate(same_tags=Count('tags')).order_by('-same_tags', '-publish')[:3]
        context = {
            'post': post,
            'similar_posts':similar_posts,
        }
        return render(request, 'blog/blog_detail.html', context=context)
