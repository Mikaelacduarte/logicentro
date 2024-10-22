from datetime import datetime

from django.db import models
from operacao.models import Operacao

class Confronto(models.Model):
    id_confronto = models.AutoField(primary_key=True)

    # Chave estrangeira para o modelo Operacao
    operacao = models.ForeignKey(Operacao, on_delete=models.PROTECT, db_column='id_operacao')  # Alinhado com o SQL

    # Data e hora do confronto
    dta_confronto = models.DateField(default=datetime.now())

    # Status do confronto
    status = models.CharField(max_length=45) #inconsistente ou concluido

    comentario = models.TextField()
    # Justificativa do confronto
    # justificativa = models.CharField(max_length=45)

    # Observação (opcional)
    # observacao = models.CharField(max_length=45, null=True, blank=True)

    class Meta:
        db_table = 'tb_confronto'  # Adicionado para refletir o nome da tabela
        indexes = [
            models.Index(fields=['operacao'], name='idx_confronto_operacao'),
        ]

    def __str__(self):
        return f"Confronto {self.id_confronto} - Operação {self.operacao.id_operacao}"
