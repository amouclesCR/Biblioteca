# Generated by Django 2.2 on 2019-04-25 02:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0009_auto_20190424_1251'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ambu_solicitud_baja',
            name='sbja_usuario',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='entidad_usuario', to='api.AMBU_Usuario'),
        ),
    ]
