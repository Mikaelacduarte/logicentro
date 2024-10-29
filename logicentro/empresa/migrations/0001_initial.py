# Generated by Django 5.1.2 on 2024-10-28 23:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Empresa',
            fields=[
                ('id_empresa', models.AutoField(primary_key=True, serialize=False)),
                ('cnpj', models.CharField(max_length=45, unique=True)),
                ('nome', models.CharField(max_length=45)),
                ('logradouro', models.CharField(max_length=45)),
                ('cidade', models.CharField(max_length=45)),
                ('estado', models.CharField(max_length=45)),
                ('situacao', models.CharField(choices=[('A', 'Ativo'), ('I', 'Inativo')], max_length=1)),
            ],
            options={
                'db_table': 'tb_empresa',
            },
        ),
    ]
