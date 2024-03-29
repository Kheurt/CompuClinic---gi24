# Generated by Django 3.2.5 on 2021-08-01 10:24

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('matricule', models.CharField(max_length=20, unique=True)),
                ('nom', models.CharField(max_length=100)),
                ('prenom', models.CharField(default='', max_length=100)),
                ('CNI', models.CharField(default='', max_length=20)),
                ('sexe', models.CharField(choices=[('H', 'Homme'), ('F', 'Femme')], default='H', max_length=1)),
                ('date_naissance', models.DateField(blank=True, null=True)),
                ('lieu_naissance', models.CharField(default='', max_length=20)),
                ('telephone', models.CharField(default='', max_length=15)),
                ('nationalite', models.CharField(default='Camerounais', max_length=50)),
                ('profession', models.CharField(default='Eleve', max_length=50)),
                ('lieu_travail', models.CharField(default='', max_length=50)),
                ('telephone_lieu_travail', models.CharField(default='', max_length=15)),
                ('domicile', models.CharField(default='', max_length=20)),
                ('nom_garant', models.CharField(default='', max_length=20)),
                ('prenom_garant', models.CharField(default='', max_length=20)),
                ('telephone_garant', models.CharField(default='', max_length=15)),
                ('adresse_garant', models.CharField(default='', max_length=50)),
                ('profession_garant', models.CharField(default='', max_length=50)),
                ('lieu_travail_garant', models.CharField(default='', max_length=50)),
                ('est_interne', models.BooleanField(default=False)),
                ('type', models.CharField(choices=[('Externe', 'Externe'), ('Interne', 'Interne')], default='Externe', max_length=10)),
                ('date_creation', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Dossier',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('matricule', models.CharField(max_length=20, unique=True)),
                ('date_creation', models.DateTimeField(auto_now_add=True)),
                ('patient', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='secretariat.patient')),
            ],
        ),
    ]
