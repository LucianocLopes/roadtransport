# Generated by Django 5.2.3 on 2025-06-19 23:01

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Record',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='Modificado em')),
                ('record_type', models.CharField(choices=[('P', 'Pessoa Física'), ('B', 'Pessoa Jurídica')], max_length=1, verbose_name='Tipo de Registro')),
                ('create_by', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL, verbose_name='Criado por')),
            ],
            options={
                'verbose_name': 'Registro',
                'verbose_name_plural': 'Registros',
            },
        ),
        migrations.CreateModel(
            name='Business',
            fields=[
                ('record_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='record.record')),
                ('name', models.CharField(max_length=254, verbose_name='Razão Social')),
                ('fantasy_name', models.CharField(max_length=150, verbose_name='Fantasia')),
                ('cnpj_number', models.CharField(max_length=14, unique=True, verbose_name='CNPJ')),
            ],
            options={
                'verbose_name': 'Empresa',
                'verbose_name_plural': 'Empresas',
            },
            bases=('record.record',),
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('record_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='record.record')),
                ('first_name', models.CharField(max_length=50, verbose_name='Primeiro Nome')),
                ('last_name', models.CharField(max_length=70, verbose_name='Sobrenome')),
                ('cpf_number', models.CharField(max_length=11, unique=True, verbose_name='CPF')),
            ],
            options={
                'verbose_name': 'Pessoa',
                'verbose_name_plural': 'Pessoas',
            },
            bases=('record.record',),
        ),
    ]
