# Generated by Django 3.2.16 on 2022-11-16 13:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0010_auto_20221114_1029'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meta_valor',
            name='meta',
            field=models.DecimalField(decimal_places=2, max_digits=8),
        ),
        migrations.AlterField(
            model_name='pipelinea',
            name='money_a',
            field=models.DecimalField(decimal_places=2, max_digits=8),
        ),
        migrations.AlterField(
            model_name='pipelineb',
            name='money_b',
            field=models.DecimalField(decimal_places=2, max_digits=8),
        ),
        migrations.AlterField(
            model_name='pipelinec',
            name='money_c',
            field=models.DecimalField(decimal_places=2, max_digits=8),
        ),
    ]
