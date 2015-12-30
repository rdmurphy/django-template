# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations


def create_site(apps, schema_editor):
    """
    Set the site's domain and name. Change below to what you need.

    """
    Site = apps.get_model("sites", "Site")
    Site.objects.update_or_create(
        id=settings.SITE_ID,
        defaults={
            "domain": "example.com",
            "name": "example.com"
        }
    )


def revert_site(apps, schema_editor):
    """
    Revert site domain and name to original settings.

    """
    Site = apps.get_model("sites", "Site")
    Site.objects.update_or_create(
        id=settings.SITE_ID,
        defaults={
            "domain": "example.com",
            "name": "example.com"
        }
    )


class Migration(migrations.Migration):

    dependencies = [
        ('sites', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_site, revert_site),
    ]
