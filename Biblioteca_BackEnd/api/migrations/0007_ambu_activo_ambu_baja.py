# Generated by Django 2.2 on 2019-04-23 13:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_auto_20190422_1817'),
    ]

    operations = [
        migrations.CreateModel(
            name='AMBU_Activo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('act_descripcion', models.CharField(max_length=500)),
                ('act_observacion', models.CharField(max_length=500)),
                ('act_numero_activo', models.CharField(max_length=50)),
                ('act_calor', models.CharField(max_length=50)),
                ('act_serie', models.CharField(max_length=50)),
                ('act_modelo', models.CharField(max_length=50)),
                ('act_marca', models.CharField(max_length=50)),
                ('act_estatus', models.BooleanField(default=False)),
                ('act_costo', models.FloatField()),
                ('act_organizacion', models.CharField(max_length=50)),
                ('act_subestatus', models.CharField(max_length=50)),
                ('act_seccion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.AMBU_Seccion')),
                ('act_usuario_responsabe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.AMBU_Usuario')),
            ],
        ),
        migrations.CreateModel(
            name='AMBU_Baja',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bja_motivos_solicitud', models.CharField(max_length=250)),
                ('bja_activo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.AMBU_Activo')),
                ('bja_baja', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.AMBU_Solicitud_Baja')),
            ],
        ),
    ]
