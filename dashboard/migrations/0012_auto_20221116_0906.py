# Generated by Django 3.2.16 on 2022-11-16 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0011_auto_20221116_0902'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meta_valor',
            name='meta',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='pipelinea',
            name='money_a',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='pipelineb',
            name='money_b',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='pipelinec',
            name='money_c',
            field=models.IntegerField(),
        ),
    ]
