# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-06-03 21:25
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=10, verbose_name='N\xfamero')),
                ('street', models.CharField(max_length=50, verbose_name='Rua')),
                ('complement', models.CharField(blank=True, max_length=150, verbose_name='Complemento')),
                ('postal_code', models.CharField(blank=True, max_length=10, verbose_name='CEP')),
                ('longitude', models.FloatField(blank=True, null=True, verbose_name='Longitude')),
                ('latitude', models.FloatField(blank=True, null=True, verbose_name='Latitude')),
            ],
            options={
                'verbose_name': 'Endere\xe7o',
                'verbose_name_plural': 'Endere\xe7os',
            },
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Nome')),
            ],
            options={
                'verbose_name': 'Cidade',
                'verbose_name_plural': 'Cidades',
            },
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cnpj', models.CharField(max_length=200, verbose_name='CNPJ')),
                ('civil_name', models.CharField(blank=True, max_length=200, verbose_name='Raz\xe3o social')),
                ('commercial_name', models.CharField(blank=True, max_length=200, null=True, verbose_name='Nome fantasia')),
                ('phone_main', models.CharField(max_length=50, verbose_name='Telefone 1')),
                ('phone_secondary', models.CharField(max_length=50, verbose_name='Telefone 2')),
                ('whatsapp', models.CharField(max_length=50, verbose_name='Whatsapp')),
                ('logo', models.ImageField(blank=True, null=True, upload_to='logos', verbose_name='Logomarca')),
                ('contact_person', models.CharField(max_length=200, verbose_name='Contato')),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
                ('website', models.CharField(max_length=254, verbose_name='Website')),
                ('twitter', models.CharField(max_length=254, verbose_name='Twitter')),
                ('facebook', models.CharField(max_length=254, verbose_name='Facebook')),
            ],
            options={
                'verbose_name': 'Empresa',
                'verbose_name_plural': 'Empresas',
            },
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Nome')),
            ],
            options={
                'verbose_name': 'Pa\xeds',
                'verbose_name_plural': 'Pa\xedses',
            },
        ),
        migrations.CreateModel(
            name='EquipmentType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=500, verbose_name='Descri\xe7\xe3o')),
            ],
            options={
                'verbose_name': 'Tipo de equipamento',
            },
        ),
        migrations.CreateModel(
            name='Inventary',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(verbose_name='Quantidade')),
                ('deliverd_date', models.DateField(verbose_name='Data de entrega')),
                ('return_date', models.DateField(verbose_name='Data de retorno')),
                ('local', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ambientalweb.Company', verbose_name='Local')),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ambientalweb.EquipmentType', verbose_name='Tipo de equipamento')),
            ],
            options={
                'verbose_name': 'Invent\xe1rio',
            },
        ),
        migrations.CreateModel(
            name='Neighborhood',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Nome')),
            ],
            options={
                'verbose_name': 'Bairro',
                'verbose_name_plural': 'Bairros',
            },
        ),
        migrations.CreateModel(
            name='Partnership',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=200, verbose_name='Tipo de parceria')),
                ('start_date', models.DateField()),
            ],
            options={
                'verbose_name': 'Parceria',
                'verbose_name_plural': 'Parcerias',
            },
        ),
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Nome')),
            ],
            options={
                'verbose_name': 'Estado',
                'verbose_name_plural': 'Estados',
            },
        ),
        migrations.AddField(
            model_name='company',
            name='partnership',
            field=models.ManyToManyField(to='ambientalweb.Partnership'),
        ),
        migrations.AddField(
            model_name='address',
            name='city',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='ambientalweb.City', verbose_name='Cidade'),
        ),
        migrations.AddField(
            model_name='address',
            name='country',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='ambientalweb.Country', verbose_name='Pa\xeds'),
        ),
        migrations.AddField(
            model_name='address',
            name='neighborhood',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ambientalweb.Neighborhood', verbose_name='Bairro'),
        ),
        migrations.AddField(
            model_name='address',
            name='state',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='ambientalweb.State', verbose_name='Estado'),
        ),
    ]
