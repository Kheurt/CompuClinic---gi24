# Generated by Django 3.2.5 on 2021-08-01 10:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('grh', '0001_initial'),
        ('consultation', '0001_initial'),
        ('secretariat', '0001_initial'),
        ('plateau_technique', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='parametre',
            name='auteur',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='grh.personnel'),
        ),
        migrations.AddField(
            model_name='parametre',
            name='consultation',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='consultation.consultation'),
        ),
        migrations.AddField(
            model_name='examen',
            name='consultation',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='consultation.consultation'),
        ),
        migrations.AddField(
            model_name='examen',
            name='laborantin',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='grh.laborantin'),
        ),
        migrations.AddField(
            model_name='differentiel',
            name='consultation',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='consultation.consultation'),
        ),
        migrations.AddField(
            model_name='consultation',
            name='dossier',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='secretariat.dossier'),
        ),
        migrations.AddField(
            model_name='consultation',
            name='medecin',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='grh.medecin'),
        ),
        migrations.AddField(
            model_name='consultation',
            name='precedant',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='consultation.consultation'),
        ),
        migrations.AddField(
            model_name='consultation',
            name='service',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='plateau_technique.service'),
        ),
        migrations.AddField(
            model_name='examen',
            name='prescription',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='consultation.prescriptionexamen'),
        ),
    ]
