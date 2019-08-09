# Generated by Django 2.2 on 2019-06-03 23:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0063_ambu_customeusuario_cus_identificacion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ambu_activo',
            name='act_usuario_responsabe',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='ambu_solicitud_baja',
            name='sbja_usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='entidad_usuario', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='ambu_solicitud_baja',
            name='sbja_usuario_nuevo',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
