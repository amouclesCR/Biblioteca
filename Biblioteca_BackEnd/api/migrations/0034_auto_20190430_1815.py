# Generated by Django 2.2 on 2019-05-01 00:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0033_ambu_usuario_usu_correo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ambu_usuario',
            name='usu_correo',
            field=models.CharField(max_length=50),
        ),
    ]
