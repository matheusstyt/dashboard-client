# # -*- coding: utf-8 -*-
# from __future__ import unicode_literals
 
from django.contrib import admin
from .models import Faturamento
 
admin.site.register(Faturamento)
  
# class EventAdmin(admin.ModelAdmin):
#     list_display = ['day', 'start_time', 'end_time', 'notes']