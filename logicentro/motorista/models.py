from django.db import models

# Create your models here.
class Motorista(models.Model):
    id_motorista = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=45)
    cpf = models.CharField(max_length=45, unique=True)
    cnh = models.CharField(max_length=45, unique=True)
    telefone = models.CharField(max_length=45, null=True, blank=True)
    SITUACAO_CHOICES = [
        ('A', 'Ativo'),
        ('I', 'Inativo'),
    ]
    situacao = models.CharField(max_length=1, choices=SITUACAO_CHOICES)

    # class Meta:
    #     db_table = 'tb_motorista'
    #
    # def __str__(self):
    #     return self.nome