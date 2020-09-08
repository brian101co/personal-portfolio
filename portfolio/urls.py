from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.sitemaps.views import sitemap
from .sitemap import StaticViewSitemap, BlogPostSitemap, ProjectSitemap

sitemaps = {
    'static': StaticViewSitemap,
    'blog': BlogPostSitemap,
    'project': ProjectSitemap,
}

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/', include('blog.urls', namespace='blog')),
    path('comments/', include('django_comments_xtd.urls')),
    path('portfolio/', include('pages.urls', namespace='portfolio')),
    path('dashboard/', include('dashboard.urls')),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
    path('', include('allauth.urls')),
    path('', include('jobs.urls', namespace='jobs')),
]


if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
