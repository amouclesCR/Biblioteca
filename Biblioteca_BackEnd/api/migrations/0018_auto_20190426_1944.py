# Generated by Django 2.2 on 2019-04-27 01:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0017_auto_20190426_1929'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ambu_activo',
            name='act_usuario_responsabe',
            field=models.ForeignKey(db_column='act_usuario_responsabe', on_delete=django.db.models.deletion.CASCADE, to='api.AMBU_Usuario'),
        ),
    ]
