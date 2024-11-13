from django.contrib import admin
from .models import Curso, Periodo, Turno, Professor, Sala, Feriado, Aula


admin.site.register(Curso)
admin.site.register(Periodo)
admin.site.register(Turno)
admin.site.register(Professor)
admin.site.register(Sala)
admin.site.register(Feriado)
admin.site.register(Aula)
