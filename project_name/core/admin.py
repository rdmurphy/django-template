# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.contrib import admin


class ReadOnlyAdmin(admin.ModelAdmin):
    """
    A ModelAdmin base that can be used to present a Model in the admin with
    only read-only fields.

    """
    def get_readonly_fields(self, *args, **kwargs):
        return [f.name for f in self.model._meta.fields]
