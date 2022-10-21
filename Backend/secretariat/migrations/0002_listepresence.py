# Generated by Django 3.2.5 on 2021-08-07 09:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('secretariat', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ListePresence',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('a_paye', models.BooleanField(default=False)),
                ('date_creation', models.DateTimeField(auto_now_add=True)),
                ('patient', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='secretariat.patient')),
            ],
        ),
    ]