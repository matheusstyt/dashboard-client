# # -*- coding: utf-8 -*-
# from __future__ import unicode_literals
 
from django.contrib import admin
from .models import Faturamento
from .models import Planejado
from .models import Curso
from .models import Concluido
from .models import Meta_Valor
from .models import Placar_Licensas
from .models import Licencas_Faltando

admin.site.register(Faturamento)
admin.site.register(Planejado)
admin.site.register(Curso)
admin.site.register(Concluido)
# admin.site.register(Meta_Valor)
# admin.site.register(Placar_Licensas)
# admin.site.register(Licencas_Faltando)
# class EventAdmin(admin.ModelAdmin):
#     list_display = ['day', 'start_time', 'end_time', 'notes']