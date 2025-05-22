from django.contrib import admin
from .models import *

@admin.register(Medicos)
class MedicosAdmin(admin.ModelAdmin):
    list_display = ['nome', 'crm', 'telefone', 'email', 'status']
    ordering = ['nome']
    search_fields = ['nome', 'crm', 'cpf', 'telefone']
    list_filter = ['status']
    readonly_fields = ['criado_em', 'atualizado_em']

@admin.register(SetorAtuacao)
class SetorAtuacaoAdmin(admin.ModelAdmin):
    list_display = ['nome', 'criado_em']
    ordering = ['nome']
    search_fields = ['nome']
    readonly_fields = ['criado_em', 'atualizado_em']

@admin.register(Enfermeiro)
class Enfermeirodmin(admin.ModelAdmin):
    list_display = ['nome', 'coren', 'telefone', 'email', 'atuacao', 'turno', 'status']
    ordering = ['nome']
    search_fields = ['nome', 'coren', 'cpf', 'telefone']
    list_filter = ['atuacao', 'turno','status']
    readonly_fields = ['criado_em', 'atualizado_em']


@admin.register(Paciente)
class PacienteAdmin(admin.ModelAdmin):
    list_display = ['nome', 'sexo', 'tipo_sanguineo', 'data_nascimento', 'cpf', 'rg','telefone_principal' , 'telefone_segundario', 'email', 'nome_mae', 'nome_pai']
    ordering = ['nome']
    search_fields = ['nome', 'cpf', 'telefone_principal','telefone_segundario', 'nome_mae','nome_pai']
    list_filter = ['tipo_sanguineo', 'sexo']
    readonly_fields = ['criado_em', 'atualizado_em']