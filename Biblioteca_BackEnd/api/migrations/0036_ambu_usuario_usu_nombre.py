# Generated by Django 2.2 on 2019-05-01 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0035_ambu_solicitud_baja_sbja_activos'),
    ]

    operations = [
        migrations.AddField(
            model_name='ambu_usuario',
            name='usu_nombre',
            field=models.CharField(default='test', max_length=50),
        ),
    ]
