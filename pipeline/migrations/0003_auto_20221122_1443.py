# Generated by Django 3.2.16 on 2022-11-22 18:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pipeline', '0002_auto_20221122_1435'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pipelinevendas',
            name='Contato',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='pipelinevendas',
            name='Data_doPC',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='pipelinevendas',
            name='Data_envio_Proposta',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='pipelinevendas',
            name='Descricao',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='pipelinevendas',
            name='Entrega',
            field=models.CharField(choices=[('Realizada', 'Realizada'), ('Pendente', 'Pendente'), ('N/A', 'N/A')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='pipelinevendas',
            name='Fase',
            field=models.CharField(choices=[('Aprovado', 'Aprovado'), ('Compras', 'Compras'), ('Negociação', 'Negociação'), ('Perdido', 'Perdido')], max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='pipelinevendas',
            name='FaturadoMesAtual',
            field=models.DecimalField(decimal_places=2, max_digits=8, null=True),
        ),
        migrations.AlterField(
            model_name='pipelinevendas',
            name='Hardware',
            field=models.DecimalField(decimal_places=2, max_digits=8, null=True),
        ),
        migrations.AlterField(
            model_name='pipelinevendas',
            name='NF_Emitidas',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='pipelinevendas',
            name='OMIE',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='pipelinevendas',
            name='Pagamento',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='pipelinevendas',
            name='Perpetua',
            field=models.DecimalField(decimal_places=2, max_digits=8, null=True),
        ),
        migrations.AlterField(
            model_name='pipelinevendas',
            name='Qtd_Coletor',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='pipelinevendas',
            name='Recorrencia',
            field=models.DecimalField(decimal_places=2, max_digits=8, null=True),
        ),
        migrations.AlterField(
            model_name='pipelinevendas',
            name='RevisaoRecente',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='pipelinevendas',
            name='Servicos',
            field=models.DecimalField(decimal_places=2, max_digits=8, null=True),
        ),
        migrations.AlterField(
            model_name='pipelinevendas',
            name='TotalPrevisto',
            field=models.DecimalField(decimal_places=2, max_digits=8, null=True),
        ),
        migrations.AlterField(
            model_name='pipelinevendas',
            name='UF',
            field=models.CharField(choices=[('RO', 'Rondônia'), ('AC', 'Acre'), ('AM', 'Amazonas'), ('RR', 'Roraima'), ('PA', 'Pará'), ('AP', 'Amapá'), ('TO', 'Tocantins'), ('MA', 'Maranhão'), ('PI', 'Piauí'), ('CE', 'Ceará'), ('RN', 'Rio Grande do Norte'), ('PB', 'Paraíba'), ('PE', 'Pernambuco'), ('AL', 'Alagoas'), ('SE', 'Sergipe'), ('BA', 'Bahia'), ('MG', 'Minas Gerais'), ('ES', 'Espírito Santo'), ('RJ', 'Rio de Janeiro'), ('SP', 'São Paulo'), ('PR', 'Paraná'), ('SC', 'Santa Catarina'), ('RS', 'Rio Grande do Sul'), ('MS', 'Mato Grosso do Sul'), ('MT', 'Mato Grosso'), ('GO', 'Goiás'), ('DF', 'Distrito Federal')], max_length=30, null=True),
        ),
    ]