# Generated by Django 2.2 on 2019-04-27 02:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0018_auto_20190426_1944'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ambu_activo',
            name='act_usuario_responsabe',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.AMBU_Usuario'),
        ),
    ]