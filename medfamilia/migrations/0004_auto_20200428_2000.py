# Generated by Django 3.0.5 on 2020-04-28 23:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medfamilia', '0003_consulta'),
    ]

    operations = [
        migrations.AlterField(
            model_name='consulta',
            name='info_adicionais',
            field=models.TextField(blank=True),
        ),
    ]