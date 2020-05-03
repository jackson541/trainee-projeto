# Generated by Django 3.0.5 on 2020-05-01 18:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medfamilia', '0011_auto_20200429_1344'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='especialidade',
            options={'ordering': ['nome']},
        ),
        migrations.RemoveField(
            model_name='especialidade',
            name='titulo',
        ),
        migrations.AddField(
            model_name='especialidade',
            name='nome',
            field=models.CharField(default='nmome', max_length=100, verbose_name='Nome'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='especialidade',
            name='descricao',
            field=models.TextField(verbose_name='Descrição'),
        ),
    ]
