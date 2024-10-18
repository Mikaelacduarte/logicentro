# Importa o módulo 'models' do Django para definir modelos de banco de dados.
from django.db import models

# Define a classe 'Motorista', que representa a tabela 'motorista' no banco de dados.
class Motorista(models.Model):
    # Define o campo 'id_motorista' como chave primária, gerado automaticamente.
    id_motorista = models.AutoField(primary_key=True)

    # Define o campo 'nome', cpf e cnh e telefone como uma string com até 45 caracteres.
    nome = models.CharField(max_length=45)
    cpf = models.CharField(max_length=45, unique=True)
    cnh = models.CharField(max_length=45, unique=True)
    telefone = models.CharField(max_length=45, null=True, blank=True)

    # Define as opções de situação como uma lista de tuplas para 'situacao'.
    SITUACAO_CHOICES = [
        ('A', 'Ativo'),   # 'A' representa motorista ativo.
        ('I', 'Inativo'), # 'I' representa motorista inativo.
    ]

    # Define o campo 'situacao' com opções limitadas às definidas em SITUACAO_CHOICES.
    situacao = models.CharField(max_length=1, choices=SITUACAO_CHOICES)

    # class Meta:
    #     db_table = 'tb_motorista'  
    #
    # def __str__(self):
    #     return self.nome  
