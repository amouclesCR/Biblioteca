# Generated by Django 2.2 on 2019-04-29 17:59

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0020_auto_20190429_1016'),
    ]

    operations = [
        migrations.AddField(
            model_name='ambu_activo',
            name='act_Fecha_Actualizado',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AddField(
            model_name='ambu_activo',
            name='act_Fecha_Creacion',
            field=models.DateField(default=datetime.date.today),
        ),
    ]