from django.conf import settings
from django.urls import include, path, re_path
from django.contrib import admin
from wagtail.documents import urls as wagtaildocs_urls
from coderedcms import admin_urls as coderedadmin_urls
from coderedcms import search_urls as coderedsearch_urls
from coderedcms import urls as codered_urls
from django.views.generic.base import TemplateView

urlpatterns = [
    # Admin
    path('admin/', include('admin_honeypot.urls', namespace='admin_honeypot')),
    path('django/', admin.site.urls),
    path('wagtail/', include(coderedadmin_urls)),

    # Documents
    path('docs/', include(wagtaildocs_urls)),

    # Search
    path('search/', include(coderedsearch_urls)),
    path('account/', include('allauth.urls')),
    path('', include('user_sessions.urls', 'user_sessions')),
    path('index/', TemplateView.as_view(template_name='base/base.html')),

    # For anything not caught by a more specific rule above, hand over to
    # the page serving mechanism. This should be the last pattern in
    # the list:
    re_path(r'', include(codered_urls)),

    # Alternatively, if you want CMS pages to be served from a subpath
    # of your site, rather than the site root:
    #    re_path(r"^pages/", include(codered_urls)),
]


if settings.DEBUG:
    from django.conf.urls.static import static
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns

    # Serve static and media files from development server
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
