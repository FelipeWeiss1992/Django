# Generated by Django 4.1.5 on 2023-01-17 00:12

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alunos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alunos',
            name='data_aluno',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
    ]