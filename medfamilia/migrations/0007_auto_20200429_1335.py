# Generated by Django 3.0.5 on 2020-04-29 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medfamilia', '0006_consulta_respondida'),
    ]

    operations = [
        migrations.AlterField(
            model_name='consulta',
            name='respondida',
            field=models.BooleanField(null=True),
        ),
    ]
