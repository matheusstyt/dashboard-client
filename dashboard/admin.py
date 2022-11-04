# # -*- coding: utf-8 -*-
# from __future__ import unicode_literals
 
from django.contrib import admin
from .models import Faturamento
from .models import Planejado
from .models import Curso
from .models import Concluido
admin.site.register(Faturamento)
admin.site.register(Planejado)
admin.site.register(Curso)
admin.site.register(Concluido)
# class EventAdmin(admin.ModelAdmin):
#     list_display = ['day', 'start_time', 'end_time', 'notes']