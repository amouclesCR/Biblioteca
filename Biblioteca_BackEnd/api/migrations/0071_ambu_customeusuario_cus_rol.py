# Generated by Django 2.2 on 2019-06-04 15:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0070_remove_ambu_customeusuario_cus_rol'),
    ]

    operations = [
        migrations.AddField(
            model_name='ambu_customeusuario',
            name='cus_rol',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='api.AMBU_Rol'),
        ),
    ]
