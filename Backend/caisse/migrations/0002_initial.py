# Generated by Django 3.2.5 on 2021-08-01 10:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('grh', '0001_initial'),
        ('caisse', '0001_initial'),
        ('secretariat', '0001_initial'),
        ('plateau_technique', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tiaps',
            name='medecin',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='grh.medecin'),
        ),
        migrations.AddField(
            model_name='tiaps',
            name='quittance',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='caisse.quittance'),
        ),
        migrations.AddField(
            model_name='tiaps',
            name='service',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='plateau_technique.service'),
        ),
        migrations.AddField(
            model_name='quittance',
            name='caissier',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='grh.caissier'),
        ),
        migrations.AddField(
            model_name='quittance',
            name='patient',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='secretariat.patient'),
        ),
        migrations.AddField(
            model_name='bon',
            name='patient',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='secretariat.patient'),
        ),
        migrations.AddField(
            model_name='bon',
            name='prestataire',
            field=models.ForeignKey(help_text='Personnel qui délivre le bon', on_delete=django.db.models.deletion.CASCADE, to='grh.personnel'),
        ),
    ]
