# Generated by Django 2.2 on 2019-05-27 21:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('admin', '0004_auto_20190527_1502'),
        ('auth', '0011_update_proxy_permissions'),
        ('api', '0058_auto_20190526_2017'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='customeUser',
            new_name='AMBU_CustomeUsuario',
        ),
        migrations.RenameField(
            model_name='ambu_customeusuario',
            old_name='permiso',
            new_name='rol',
        ),
    ]
