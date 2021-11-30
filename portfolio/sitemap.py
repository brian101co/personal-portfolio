from django.contrib.sitemaps import Sitemap
from django.shortcuts import reverse
from projects.models import Project

class ProjectSitemap(Sitemap):
    changefreq = "never"
    priority = 0.9

    def items(self):
        return Project.objects.all()

    def lastmod(self, obj):
        return obj.completed_date

class StaticViewSitemap(Sitemap):
    def items(self):
        return ['hire-me', 'home']

    def location(self, item):
        return reverse(item)