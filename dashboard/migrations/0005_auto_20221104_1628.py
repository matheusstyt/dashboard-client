# Generated by Django 2.1.15 on 2022-11-04 20:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0004_auto_20221104_1552'),
    ]

    operations = [
        migrations.AlterField(
            model_name='concluido',
            name='descricao_concluido',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='curso',
            name='descricao_curso',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='planejado',
            name='descricao_planejado',
            field=models.TextField(),
        ),
    ]
