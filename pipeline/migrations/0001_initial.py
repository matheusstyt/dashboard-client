# Generated by Django 3.2.16 on 2022-11-22 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PipelineVendas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateField(auto_now=True)),
                ('updated_at', models.DateField(auto_now_add=True)),
                ('Cliente', models.CharField(max_length=255)),
                ('UF', models.CharField(choices=[('RO', 'Rondônia'), ('AC', 'Acre'), ('AM', 'Amazonas'), ('RR', 'Roraima'), ('PA', 'Pará'), ('AP', 'Amapá'), ('TO', 'Tocantins'), ('MA', 'Maranhão'), ('PI', 'Piauí'), ('CE', 'Ceará'), ('RN', 'Rio Grande do Norte'), ('PB', 'Paraíba'), ('PE', 'Pernambuco'), ('AL', 'Alagoas'), ('SE', 'Sergipe'), ('BA', 'Bahia'), ('MG', 'Minas Gerais'), ('ES', 'Espírito Santo'), ('RJ', 'Rio de Janeiro'), ('SP', 'São Paulo'), ('PR', 'Paraná'), ('SC', 'Santa Catarina'), ('RS', 'Rio Grande do Sul'), ('MS', 'Mato Grosso do Sul'), ('MT', 'Mato Grosso'), ('GO', 'Goiás'), ('DF', 'Distrito Federal')], max_length=30)),
                ('Fase', models.CharField(choices=[('aprovado', 'Aprovado'), ('negociacao', 'Negociação'), ('perdido', 'Perdido')], max_length=10)),
                ('Descricao', models.CharField(max_length=100)),
                ('OMIE', models.CharField(max_length=100)),
                ('NF_Emitidas', models.CharField(max_length=100)),
                ('Qtd_Coletor', models.IntegerField()),
                ('Data_envio_Proposta', models.DateField()),
                ('RevisaoRecente', models.CharField(max_length=50)),
                ('Data_doPC', models.DateField()),
                ('Recorrencia', models.DecimalField(decimal_places=2, max_digits=8)),
                ('Perpetua', models.DecimalField(decimal_places=2, max_digits=8)),
                ('Hardware', models.DecimalField(decimal_places=2, max_digits=8)),
                ('Servicos', models.DecimalField(decimal_places=2, max_digits=8)),
                ('TotalPrevisto', models.DecimalField(decimal_places=2, max_digits=8)),
                ('FaturadoMesAtual', models.DecimalField(decimal_places=2, max_digits=8)),
                ('Entrega', models.CharField(max_length=50)),
                ('Pagamento', models.CharField(max_length=50)),
                ('Contato', models.CharField(max_length=50)),
                ('OBS', models.TextField()),
            ],
        ),
    ]
