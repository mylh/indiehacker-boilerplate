from django.contrib import sitemaps
from django.urls import reverse

# from .models import MyModel


# class SamplesSitemap(sitemaps.Sitemap):
#     changefreq = "weekly"
#     priority = 0.5

#     def items(self):
#         return MyModel.objects.filter(is_visible=True)

#     def location(self, item):
#         return reverse("samples", args=[item.pk])

#     def lastmod(self, obj):
#         return obj.updated_at


class StaticViewSitemap(sitemaps.Sitemap):
    priority = 1
    changefreq = "daily"

    def items(self):
        return ["index", "terms"]

    def location(self, item):
        return reverse(item)
