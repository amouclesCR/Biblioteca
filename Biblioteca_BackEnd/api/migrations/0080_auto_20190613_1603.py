# Generated by Django 2.2 on 2019-06-13 22:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0079_delete_ambu_usuario'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ambu_customeusuario',
            name='cus_rol',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='api.AMBU_Rol'),
        ),
    ]