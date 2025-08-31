from django.contrib import admin
from .models import Estudiante


@admin.register(Estudiante)
class EstudianteAdmin(admin.ModelAdmin):
    list_display = ("id", "nombre", "carrera", "ciclo", "correo")
    search_fields = ("nombre", "correo")
    list_filter = ("carrera", "ciclo")