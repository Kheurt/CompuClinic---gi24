# Generated by Django 3.2.5 on 2021-08-31 18:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('consultation', '0002_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='consultation',
            name='en_cours',
            field=models.BooleanField(default=True),
        ),
    ]
