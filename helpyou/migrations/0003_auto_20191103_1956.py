# Generated by Django 2.2.6 on 2019-11-03 22:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('helpyou', '0002_tb_salas'),
    ]

    operations = [
        migrations.CreateModel(
            name='TB_psicologos',
            fields=[
                ('nome', models.CharField(max_length=100)),
                ('cpf', models.IntegerField(primary_key=True, serialize=False, verbose_name=11)),
                ('registro_crp', models.IntegerField(verbose_name=100)),
                ('email', models.EmailField(max_length=254)),
                ('senha', models.CharField(max_length=18)),
                ('telefone', models.IntegerField(verbose_name=11)),
            ],
        ),
        migrations.RemoveField(
            model_name='tb_salas',
            name='id',
        ),
        migrations.AddField(
            model_name='tb_salas',
            name='cod_sala',
            field=models.AutoField(default=1, primary_key=True, serialize=False),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='tb_salas',
            name='admin',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='helpyou.TB_psicologos'),
        ),
        migrations.CreateModel(
            name='TB_participantes',
            fields=[
                ('nome', models.CharField(max_length=100)),
                ('cpf', models.IntegerField(primary_key=True, serialize=False, verbose_name=11)),
                ('email', models.EmailField(max_length=254)),
                ('senha', models.CharField(max_length=18)),
                ('telefone', models.IntegerField(verbose_name=11)),
                ('disturbio', models.TextField(blank=True, null=True)),
                ('sala_inserido', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='helpyou.TB_salas')),
            ],
        ),
    ]