# Generated by Django 2.2 on 2019-05-01 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0036_ambu_usuario_usu_nombre'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ambu_usuario',
            name='usu_nombre',
            field=models.CharField(max_length=50),
        ),
    ]
