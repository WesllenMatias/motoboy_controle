from django.db import models
from django.db.models.base import Model
from django.db.models.deletion import CASCADE
from django.db.models.fields import CharField, DateField, IntegerField
from django.db.models.fields.related import ForeignKey
from djmoney.models.fields import MoneyField


class Entregador(models.Model):
    tipo_sexo = (
        ('M', 'Masculino'),
        ('F', 'Feminino'),
        ('T', 'Trans'),
        ('A', 'Alien'),
    )

    tipo_cnh = (
        ('A','Categoria A'),
        ('B','Categoria B'),
        ('C','Categoria C'),
        ('D','Categoria D'),
        ('E','Categoria E'),
        ('AB','Categoria AB'),
    )
    
    nome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=11)
    telefone = models.CharField(max_length=9)
    dt_nascimento = models.DateField(blank=True,null=True, verbose_name='Data de Nascimento')
    sexo = models.CharField(max_length=1, choices=tipo_sexo)
    cnh = models.CharField(max_length=2, choices=tipo_cnh, verbose_name='Categoria CNH')
    dt_criacao = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name_plural = 'Cadastro de Entregadores'

    def __str__(self) -> str:
        return self.nome

    
class Marcas(models.Model):
    descricao = models.CharField(max_length=100)
    dt_criacao = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Cadastro de Marcas'
    
    def __str__(self) -> str:
        return self.descricao


class Modelos(models.Model):
    descricao = models.CharField(max_length=100)
    dt_criacao = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Cadastro de Modelos'
    
    def __str__(self) -> str:
        return self.descricao
    
    
class Veiculo(models.Model):
    tipo_veiculo = (
        ('A','Carro'),
        ('B','Moto'),
        ('C', 'Caminhão'),
        ('D', 'Van de Carga'),
        ('E', 'Carreta'),
    )
    
    descricao = models.CharField(max_length=100)
    placa = models.CharField(max_length=8)
    marca = models.ForeignKey(Marcas, on_delete=CASCADE)
    cor = models.CharField(max_length=80)
    ano = models.CharField(max_length=9)
    modelo = models.ForeignKey(Modelos, on_delete=CASCADE)
    categoria = models.CharField(max_length=1, choices=tipo_veiculo)
    km_litro = models.IntegerField(verbose_name='KM/Litro')
    dt_criacao = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name_plural = 'Cadastro de Veiculos'
    
    def __str__(self) -> str:
        return self.descricao
    
    
class Entregas(models.Model):
    cliente = models.CharField(max_length=100)
    origem = models.CharField(max_length=100)
    destino = models.CharField(max_length=100)
    data = models.DateField()
    entregador = models.ForeignKey(Entregador, on_delete=CASCADE)
    qtd_entrega = models.IntegerField()
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    
    class Meta:
        verbose_name_plural = 'Entregas'
    
    def __str__(self) -> str:
        return self.cliente
    