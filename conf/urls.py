from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from debug_toolbar.toolbar import debug_toolbar_urls

from django.views.generic import TemplateView

urlpatterns = [
    path("", TemplateView.as_view(template_name="home.html"), name="home"),
    path("admin/", admin.site.urls),
    path("__reload__/", include("django_browser_reload.urls")),
] + debug_toolbar_urls()

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
