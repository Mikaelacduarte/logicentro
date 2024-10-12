from django.db import models

# Create your models here.
class Empresa(models.Model):
    id_empresa = models.AutoField(primary_key=True)
    cnpj = models.CharField(max_length=45, unique=True)
    nome = models.CharField(max_length=45)
    logradouro = models.CharField(max_length=45)
    cidade = models.CharField(max_length=45)
    estado = models.CharField(max_length=45)
    SITUACAO_CHOICES = [
        ('A', 'Ativo'),
        ('I', 'Inativo'),
    ]
    situacao = models.CharField(max_length=1, choices=SITUACAO_CHOICES)

    # class Meta:
    #     db_table = 'tb_empresa'
    #
    # def __str__(self):
    #     return self.nome