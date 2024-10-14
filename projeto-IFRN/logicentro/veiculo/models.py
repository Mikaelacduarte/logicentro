from django.db import models  # Importa o módulo para trabalhar com modelos de banco de dados no Django.

# Criação do modelo Veiculo
class Veiculo(models.Model):  # Define a classe Veiculo como um modelo de banco de dados.
    id_veiculo = models.AutoField(primary_key=True)  # Cria um campo auto-incremental que serve como chave primária.
    placa = models.CharField(max_length=45)  # Define um campo de texto para a placa do veículo.
    marca = models.CharField(max_length=45)  # Define um campo de texto para a marca do veículo.
    modelo = models.CharField(max_length=45)  # Define um campo de texto para o modelo do veículo.
    ano = models.IntegerField()  # Define um campo numérico para o ano do veículo (corrigido: max_length não é necessário aqui).
    tipo_veiculo = models.CharField(max_length=45)  # Define um campo de texto para o tipo do veículo.
    
    # Define as opções de situação do veículo
    SITUACAO_CHOICES = [  # Lista de escolhas possíveis para a situação do veículo.
        ('A', 'Ativo'),  # 'A' para ativo
        ('I', 'Inativo'),  # 'I' para inativo
    ]
    situacao = models.CharField(max_length=1, choices=SITUACAO_CHOICES)  # Define um campo para a situação do veículo com as opções.

    # class Meta:  
    #     db_table = 'tb_veiculo'
