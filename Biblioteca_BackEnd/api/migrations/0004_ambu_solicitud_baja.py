# Generated by Django 2.2 on 2019-04-22 23:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_delete_ambu_seccionwww'),
    ]

    operations = [
        migrations.CreateModel(
            name='AMBU_Solicitud_Baja',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sbja_fecha_solicitud', models.DateField()),
                ('sbja_estado_solicitud', models.BooleanField(default=False)),
            ],
        ),
    ]
