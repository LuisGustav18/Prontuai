from django.contrib import admin
from .models import Medico

# Register your models here.
@admin.register(Medico)
class MedicoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'crm', 'especialidades', 'criado_em')
