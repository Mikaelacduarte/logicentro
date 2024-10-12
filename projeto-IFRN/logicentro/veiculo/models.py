from django.db import models

# Create your models here.
class Veiculo(models.Model):
    id_veiculo = models.AutoField(primary_key=True)
    placa = models.CharField(max_length=45)
    marca = models.CharField(max_length=45)
    modelo = models.CharField(max_length=45)
    ano = models.IntegerField(max_length=4)
    tipo_veiculo = models.CharField(max_length=45)
    SITUACAO_CHOICES = [
        ('A', 'Ativo'),
        ('I', 'Inativo'),
    ]
    situacao = models.CharField(max_length=1, choices=SITUACAO_CHOICES)

    # class Meta:
    #     db_table = 'tb_veiculo'