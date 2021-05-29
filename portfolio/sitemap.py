from django.contrib.sitemaps import Sitemap
from django.shortcuts import reverse
from projects.models import Job

class ProjectSitemap(Sitemap):
    changefreq = "never"
    priority = 0.9

    def items(self):
        return Job.objects.all()

    def lastmod(self, obj):
        return obj.created

class StaticViewSitemap(Sitemap):
    def items(self):
        return ['jobs:hire-me', 'jobs:job-list']

    def location(self, item):
        return reverse(item)