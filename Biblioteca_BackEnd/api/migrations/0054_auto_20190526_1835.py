# Generated by Django 2.2 on 2019-05-27 00:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0053_auto_20190526_1607'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='custome',
            name='groups',
        ),
        migrations.RemoveField(
            model_name='custome',
            name='user_permissions',
        ),
        migrations.DeleteModel(
            name='customeQ',
        ),
        migrations.DeleteModel(
            name='custome',
        ),
    ]
