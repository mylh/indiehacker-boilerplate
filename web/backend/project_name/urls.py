from django.conf import settings
from django.conf.urls import include
from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from django.urls import path, re_path
from django.contrib.auth.decorators import login_required
from django.views.static import serve
import django_js_reverse.views

from core import sitemaps as core_sitemaps

# from rest_framework.routers import DefaultRouter
# from core.routes import routes as core_routes

# router = DefaultRouter()

# routes = core_routes
# for route in routes:
#     router.register(
#         route["regex"], route["viewset"], basename=route["basename"]
#     )


@login_required
def protected_serve(request, path, document_root=None, show_indexes=False):
    return serve(request, path, document_root, show_indexes)


sitemaps = {
    "static": core_sitemaps.StaticViewSitemap,
    # "samples": core_sitemaps.SamplesSitemap,
}

urlpatterns = [
    path("", include("core.urls"), name="core"),
    path(
        "sitemap.xml",
        sitemap,
        {"sitemaps": sitemaps},
        name="django.contrib.sitemaps.views.sitemap",
    ),
    # !!! custom path to django admin
    path("my_{{ project_name}}_admin/", admin.site.urls, name="admin"),
    path("jsreverse/", django_js_reverse.views.urls_js, name="js_reverse"),
    # serve media files for logged in users only
    re_path(
        r"^%s(?P<path>.*)$" % settings.MEDIA_URL[1:],
        protected_serve,
        {"document_root": settings.MEDIA_ROOT},
    ),
    # path("api/", include(router.urls), name="api"),
]
