# Generated by Django 2.2.6 on 2019-11-03 02:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('helpyou', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TB_salas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('admin', models.CharField(max_length=50)),
                ('descricao', models.TextField()),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='helpyou.TD_categorias')),
            ],
        ),
    ]
