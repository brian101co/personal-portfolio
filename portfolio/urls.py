from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.sitemaps.views import sitemap
from .sitemap import StaticViewSitemap, ProjectSitemap
from django.views.generic.base import TemplateView

sitemaps = {
    'static': StaticViewSitemap,
    'project': ProjectSitemap,
}

urlpatterns = [
    path('admin/', admin.site.urls),
    path('comments/', include('django_comments_xtd.urls')),
    path('portfolio/', include('pages.urls', namespace='portfolio')),
    path('dashboard/', include('dashboard.urls')),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
    path('robots.txt', TemplateView.as_view(template_name="robots.txt", content_type="text/plain")),
    path('', include('allauth.urls')),
    path('', include('projects.urls', namespace='projects')),
]


if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
