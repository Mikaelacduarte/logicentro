from django.db import models
from empresa.models import Empresa
from motorista.models import Motorista
from veiculo.models import Veiculo
from usuario.models import Usuario

class Operacao(models.Model):
    id_operacao = models.AutoField(primary_key=True)

    veiculo = models.ForeignKey(Veiculo, on_delete=models.PROTECT, db_column='id_veiculo')
    placa = models.CharField(max_length=45)

    motorista = models.ForeignKey(Motorista, on_delete=models.PROTECT, db_column='id_motorista')

    empresa_origem = models.ForeignKey(Empresa, related_name='empresa_origem', on_delete=models.PROTECT, db_column='id_empresa_origem')

    user_saida=models.ForeignKey(Usuario, related_name='user_saida', on_delete=models.PROTECT, db_column='id_usuario_saida', null=True)
    dta_saida = models.DateField()

    empresa_destino = models.ForeignKey(Empresa, related_name='empresa_destino', on_delete=models.PROTECT, db_column='id_empresa_destino')

    user_entrada=models.ForeignKey(Usuario, related_name='user_entrada', on_delete=models.PROTECT, db_column='id_usuario_entrada', null=True)
    dta_entrada = models.DateField()

    status = models.CharField(max_length=45, default="Pendente") #Quando faz o confronto fica como Concluído

    nro_mdfe_saida = models.IntegerField(null=True, blank=True)
    nro_notafiscal_saida = models.IntegerField(null=True, blank=True)
    nro_lacre1_saida = models.IntegerField(null=True, blank=True)
    nro_lacre2_saida = models.IntegerField(null=True, blank=True)

    nro_mdfe_entrada = models.IntegerField(null=True, blank=True)
    nro_notafiscal_entrada = models.IntegerField(null=True, blank=True)
    nro_lacre1_entrada = models.IntegerField(null=True, blank=True)
    nro_lacre2_entrada = models.IntegerField(null=True, blank=True)

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
