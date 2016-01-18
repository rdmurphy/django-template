# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.views import defaults as default_views
from django.views.generic import TemplateView


urlpatterns = [
    url(r'^$', TemplateView.as_view(
        template_name='landing.html'), name='landing'),

    url(settings.ADMIN_URL, include(admin.site.urls)),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Test pages normally not reachable when DEBUG = True
if settings.DEBUG:
    urlpatterns += [
        url(r'^400/$', default_views.bad_request, {'exception':
            Exception('Bad request')}),
        url(r'^403/$', default_views.permission_denied, {'exception':
            Exception('Permission denied')}),
        url(r'^404/$', default_views.page_not_found, {'exception':
            Exception('Page not found')}),
        url(r'^500/$', default_views.server_error),
    ]
