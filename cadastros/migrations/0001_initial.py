# Generated by Django 4.2.3 on 2023-08-12 13:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sabor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sabor', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Macarons',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=40)),
                ('descricao', models.CharField(max_length=40, verbose_name='Descrição')),
                ('tamanho', models.FloatField(max_length=10)),
                ('sabor', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='cadastros.sabor')),
            ],
        ),
        migrations.CreateModel(
            name='Doces',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=40)),
                ('descricao', models.CharField(max_length=40, verbose_name='Descrição')),
                ('tamanho', models.FloatField(max_length=10)),
                ('sabor', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='cadastros.sabor')),
            ],
        ),
        migrations.CreateModel(
            name='Bolos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=40)),
                ('descricao', models.CharField(max_length=40, verbose_name='Descrição')),
                ('tamanho', models.FloatField(max_length=10)),
                ('observacao', models.TextField(blank=True, max_length=50, verbose_name='Observações')),
                ('sabor', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='cadastros.sabor')),
            ],
        ),
    ]
