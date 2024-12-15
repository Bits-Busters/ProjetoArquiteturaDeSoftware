# Generated by Django 5.1.4 on 2024-12-15 15:10

import SAFERapp.models
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('Id', models.AutoField(primary_key=True, serialize=False)),
                ('Nome', models.CharField(max_length=100)),
                ('Senha', models.CharField(max_length=100)),
                ('Email', models.CharField(max_length=100)),
                ('relacao_ufrpe', models.CharField(choices=[('docente', 'Docente'), ('discente', 'Discente'), ('tecnico', 'Técnico'), ('terceirizado', 'Terceirizado'), ('visitante', 'Visitante')], default='visitante', max_length=20, verbose_name='Relação com a UFRPE')),
            ],
        ),
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='Email')),
                ('nome', models.CharField(max_length=100, verbose_name='Nome')),
                ('telefone', models.CharField(max_length=15, verbose_name='Telefone')),
                ('telefone_fixo', models.CharField(blank=True, max_length=15, verbose_name='Telefone Fixo')),
                ('relacao_ufrpe', models.CharField(choices=[('docente', 'Docente'), ('discente', 'Discente'), ('tecnico', 'Técnico'), ('terceirizado', 'Terceirizado'), ('visitante', 'Visitante')], default='visitante', max_length=20, verbose_name='Relação com a UFRPE')),
                ('tipo_usuario', models.CharField(choices=[('admin', 'Administrador'), ('gestor', 'Gestor'), ('analista', 'Analista'), ('comum', 'Comum')], default='comum', max_length=20, verbose_name='Tipo de Usuário')),
            ],
            options={
                'abstract': False,
            },
            managers=[
                ('objects', SAFERapp.models.CustomUserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('Id', models.AutoField(primary_key=True, serialize=False)),
                ('Titulo', models.CharField(max_length=100)),
                ('Texto', models.TextField()),
                ('Data', models.DateTimeField()),
                ('Id_Autor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SAFERapp.usuario')),
            ],
        ),
        migrations.CreateModel(
            name='Ocorrencia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Descricao', models.TextField()),
                ('Local', models.CharField(max_length=100)),
                ('DataHora', models.DateTimeField()),
                ('Status', models.CharField(choices=[('aberto', 'Aberto'), ('em_analise', 'Em análise'), ('fechado', 'Fechado')], default='aberto', max_length=20, verbose_name='Status do chamado')),
                ('Autor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SAFERapp.usuario')),
            ],
        ),
    ]
