# Generated by Django 2.2 on 2019-04-30 23:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0030_auto_20190430_1735'),
    ]

    operations = [
        migrations.AddField(
            model_name='ambu_seccion',
            name='sec_departamento',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='api.AMBU_Departamento'),
        ),
    ]
