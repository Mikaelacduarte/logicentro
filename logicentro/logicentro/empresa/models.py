# Importa o módulo 'models' do Django, que é usado para definir os modelos do banco de dados.
from django.db import models

# Define a classe 'Empresa', que representa a tabela 'empresa' no banco de dados.
class Empresa(models.Model):
    
    # Define o campo 'id_empresa' como chave primária, que será um número automático gerado pelo Django.
    id_empresa = models.AutoField(primary_key=True)

    # Define o campo 'cnpj' como uma string, com um máximo de 45 caracteres e único (não pode haver duplicatas).
    cnpj = models.CharField(max_length=45, unique=True)

    # Define o campo 'nome' como uma string, com um máximo de 45 caracteres.
    nome = models.CharField(max_length=45)

    # Define o campo 'logradouro' como uma string, com um máximo de 45 caracteres (endereço).
    logradouro = models.CharField(max_length=45)

    # Define o campo 'cidade' como uma string, com um máximo de 45 caracteres.
    cidade = models.CharField(max_length=45)

    # Define o campo 'estado' como uma string, com um máximo de 45 caracteres.
    estado = models.CharField(max_length=45)

    # Define as opções de situação como uma lista de tuplas, onde cada tupla contém um valor e uma descrição.
    SITUACAO_CHOICES = [
        ('A', 'Ativo'),   # 'A' representa que a empresa está ativa.
        ('I', 'Inativo'), # 'I' representa que a empresa está inativa.
    ]
    
    # Define o campo 'situacao' como uma string, com um máximo de 1 caractere, 
    # e permite escolher entre as opções definidas em SITUACAO_CHOICES.
    situacao = models.CharField(max_length=1, choices=SITUACAO_CHOICES)

    # class Meta:
    #     db_table = 'tb_empresa'

    # def __str__(self):
    #     return self.nome 
