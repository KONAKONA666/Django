# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import *

admin.site.register(Customer)
admin.site.register(Marathon)
admin.site.register(Club)
admin.site.register(Product)


# Register your models here.
