from django.db import models
from empresa.models import Empresa
from motorista.models import Motorista
from usuario.models import Usuario
from veiculo.models import Veiculo

class Operacao(models.Model):
    id_operacao = models.AutoField(primary_key=True)

    veiculo = models.ForeignKey(Veiculo, on_delete=models.PROTECT, db_column='id_veiculo')
    placa = models.CharField(max_length=45)

    motorista = models.ForeignKey(Motorista, on_delete=models.PROTECT, db_column='id_motorista')

    empresa_origem = models.ForeignKey(Empresa, related_name='empresa_origem', on_delete=models.PROTECT, db_column='id_empresa_origem')

    dta_saida = models.DateTimeField()

    usu_cadsaida = models.ForeignKey(Usuario, related_name='usuario_saida', on_delete=models.PROTECT, db_column='usu_cadsaida')

    empresa_destino = models.ForeignKey(Empresa, related_name='empresa_destino', on_delete=models.PROTECT, db_column='id_empresa_destino')

    dta_entrada = models.DateTimeField()

    usu_cadentrada = models.ForeignKey(Usuario, related_name='usuario_entrada', on_delete=models.PROTECT, db_column='usu_cadentrada')

    status = models.CharField(max_length=45)

    nro_mdfe = models.IntegerField(null=True, blank=True)
    nro_notafiscal = models.IntegerField(null=True, blank=True)

    nro_lacre = models.IntegerField()

    class Meta:
        # db_table = 'tb_operacao'  # Alinhado com o SQL
        indexes = [
            models.Index(fields=['veiculo'], name='idx_operacao_veiculo'),
            models.Index(fields=['motorista'], name='idx_operacao_motorista'),
            models.Index(fields=['empresa_origem'], name='idx_operacao_origem'),
            models.Index(fields=['empresa_destino'], name='idx_operacao_destino'),
            models.Index(fields=['usu_cadsaida'], name='idx_operacao_saida'),
            models.Index(fields=['usu_cadentrada'], name='idx_operacao_entrada'),
        ]

    def __str__(self):
        return f"Operação {self.id_operacao} - {self.placa}"
