# Generated by Django 5.1.2 on 2024-10-20 17:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('operacao', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='operacao',
            name='dta_entrada',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='operacao',
            name='dta_saida',
            field=models.DateField(),
        ),
    ]
