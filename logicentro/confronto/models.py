from django.db import models
from operacao.models import Operacao
from usuario.models import Usuario

class Confronto(models.Model):
    id_confronto = models.AutoField(primary_key=True)

    # Chave estrangeira para o modelo Operacao
    operacao = models.ForeignKey(Operacao, on_delete=models.PROTECT, db_column='id_operacao')  # Alinhado com o SQL

    # Chave estrangeira para o modelo Usuario (usuário que fez o confronto)
    usu_confronto = models.ForeignKey(Usuario, on_delete=models.PROTECT, db_column='usu_confronto')

    # Data e hora do confronto
    dta_confronto = models.DateTimeField()

    # Situação do confronto
    situacao = models.CharField(max_length=45)

    # Justificativa do confronto
    justificativa = models.CharField(max_length=45)

    # Observação (opcional)
    observacao = models.CharField(max_length=45, null=True, blank=True)

    class Meta:
        # db_table = 'tb_confronto'  # Adicionado para refletir o nome da tabela
        indexes = [
            models.Index(fields=['operacao'], name='idx_confronto_operacao'),
            models.Index(fields=['usu_confronto'], name='idx_confronto_usuario'),
        ]

    def __str__(self):
        return f"Confronto {self.id_confronto} - Operação {self.operacao.id_operacao}"
