# Generated by Django 3.2.16 on 2022-11-25 12:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Produtos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=90)),
                ('faturamento', models.DecimalField(decimal_places=2, max_digits=8)),
                ('quantidade_absoluta', models.IntegerField()),
            ],
        ),
    ]
