from django.db import models
from empresa.models import Empresa
from motorista.models import Motorista
from veiculo.models import Veiculo

class Operacao(models.Model):
    id_operacao = models.AutoField(primary_key=True)

    veiculo = models.ForeignKey(Veiculo, on_delete=models.PROTECT, db_column='id_veiculo')
    placa = models.CharField(max_length=45)

    motorista = models.ForeignKey(Motorista, on_delete=models.PROTECT, db_column='id_motorista')

    empresa_origem = models.ForeignKey(Empresa, related_name='empresa_origem', on_delete=models.PROTECT, db_column='id_empresa_origem')

    dta_saida = models.DateField()

    empresa_destino = models.ForeignKey(Empresa, related_name='empresa_destino', on_delete=models.PROTECT, db_column='id_empresa_destino')

    dta_entrada = models.DateField()

    status = models.CharField(max_length=45, default="Pendente") #Quadno faz o confronto fica como Concluído

    nro_mdfe = models.IntegerField(null=True, blank=True)
    nro_notafiscal = models.IntegerField(null=True, blank=True)

    nro_lacre = models.IntegerField(null=True, blank=True)

    class Meta:
        db_table = 'tb_operacao'  # Alinhado com o SQL
        indexes = [
            models.Index(fields=['veiculo'], name='idx_operacao_veiculo'),
            models.Index(fields=['motorista'], name='idx_operacao_motorista'),
            models.Index(fields=['empresa_origem'], name='idx_operacao_origem'),
            models.Index(fields=['empresa_destino'], name='idx_operacao_destino'),
        ]

    def __str__(self):
        return f"Operação {self.id_operacao} - {self.placa}"
