# Generated by Django 3.2.5 on 2021-08-29 23:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('plateau_technique', '0002_auto_20210829_1400'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='local',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='plateau_technique.local'),
        ),
    ]