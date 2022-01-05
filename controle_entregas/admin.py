from django.contrib import admin
from admin_totals.admin import ModelAdminTotals
from django.contrib.admin.decorators import action
from django.db.models.aggregates import Sum
from controle_entregas.models import Entregador, Entregas, Marcas, Modelos, Veiculo
from django.db.models.functions import Coalesce

# Register your models here.
@admin.register(Entregador)
class Entregador(admin.ModelAdmin):
    actions=None
    list_display=['nome',
                  'cpf',
                  'telefone',
                  'dt_nascimento'
                  ,'sexo',
                  'cnh',]
    
    
@admin.register(Marcas)
class Marcas(admin.ModelAdmin):    
    actions=None
    list_display=['descricao',]
    seach_fields=['descricao',]
        
        
@admin.register(Modelos)
class Modelos(admin.ModelAdmin):
    actions=None
    list_display=['descricao',]
    seach_fields=['descricao',]
    

@admin.register(Veiculo)
class Veiculos(admin.ModelAdmin):
    actions=None
    list_display=[
        'descricao',
        'placa',
        'marca',
        'modelo',
    ]
    
    
@admin.register(Entregas)
class EntregasAdmin(ModelAdminTotals):
    list_display=['cliente',
                  'origem',
                  'destino',
                  'data',
                  'entregador',
                  'qtd_entrega',
                  'valor']
    list_totals = [('Total', lambda field: Coalesce(Sum(field), 0)),('valor',Sum)]
    
