from django.contrib import admin
from .models import *

@admin.register(Paciente)
class PacienteAdmin(admin.ModelAdmin):
    list_display = ('nome', 'idade', '_ambulatorio')
    exclude = ['idamb']

    def _ambulatorio(self, instance):
        return instance.idamb.nome


@admin.register(Convenio)
class ConvenioAdmin(admin.ModelAdmin):
    list_display = ('codconv', 'nome', )


@admin.register(Possui)
class PossuiAdmin(admin.ModelAdmin):
    list_display = ('paciente', 'convenio', 'tipo', 'vencimento',)
    raw_id_fields = ('paciente',)


@admin.register(Medico)
class MedicoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'crm', 'especialidade')
    list_filter = ['especialidade', 'nome']


@admin.register(Ambulatorio)
class AmbulatorioAdmin(admin.ModelAdmin):
    list_display = ('nome', 'numleitos', 'andar')
    list_filter = ('andar', 'nome')


@admin.register(Atende)
class AtendeAdmin(admin.ModelAdmin):
    list_display = ('medico', 'convenio')


@admin.register(Consulta)
class ConsultaAdmin(admin.ModelAdmin):
    list_display = ('paciente', 'medico', 'data', 'horario')
    raw_id_fields = ('paciente', 'medico')
    ordering = ('data', 'horario')


