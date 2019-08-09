# Generated by Django 2.2 on 2019-05-15 16:41

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0046_auto_20190514_1109'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ambu_activo',
            name='act_Fecha_Actualizado',
            field=models.DateTimeField(default=datetime.date.today),
        ),
        migrations.AlterField(
            model_name='ambu_activo',
            name='act_Fecha_Creacion',
            field=models.DateTimeField(default=datetime.date.today),
        ),
        migrations.AlterField(
            model_name='ambu_solicitud_baja',
            name='sbja_fecha_solicitud',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='ambu_usuario',
            name='usu_fecha',
            field=models.DateTimeField(default=datetime.date.today),
        ),
    ]
