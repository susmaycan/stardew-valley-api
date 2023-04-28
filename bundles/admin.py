# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from bundles.models import Bundle, BundleItem, BundleRoom

# Register your models here.
admin.site.register(BundleRoom)
admin.site.register(BundleItem)
admin.site.register(Bundle)
