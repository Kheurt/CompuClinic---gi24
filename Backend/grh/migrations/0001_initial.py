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
            name='Absence',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('date_heure', models.DateTimeField()),
                ('justificatif', models.TextField(blank=True, default='')),
            ],
        ),
        migrations.CreateModel(
            name='Permission',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('date_prise_permission', models.DateField()),
                ('date_retour', models.DateField(blank=True)),
                ('duree', models.DurationField()),
                ('justificatif', models.TextField()),
                ('date_creation', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Personnel',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('type_personnel', models.CharField(choices=[('Medecin', 'Médecin'), ('Caissier', 'Caissier'), ('Secretaire', 'Sécrétaire'), ('Infirmer', 'Infirmier'), ('Laborantin', 'Laborantin'), ('Stagiaire', 'Stagiaire')], default='', max_length=20)),
                ('nom', models.CharField(max_length=50)),
                ('prenom', models.CharField(max_length=50)),
                ('matricule', models.CharField(max_length=20, unique=True)),
                ('etat_civil', models.CharField(choices=[('MR', 'M.'), ('MME', 'Mme.'), ('MLLE', 'Mlle.')], default='MR', max_length=5)),
                ('date_naissance', models.DateField()),
                ('lieu_naissance', models.CharField(max_length=50)),
                ('nationalite', models.CharField(max_length=50)),
                ('domicile', models.CharField(max_length=50)),
                ('date_creation', models.DateTimeField(auto_now_add=True)),
                ('email', models.EmailField(max_length=50)),
                ('CNI', models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Pointage',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('date_heure', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Poste',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('nom', models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='ProfilSpecialiste',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('specialite', models.CharField(max_length=50)),
                ('expertise', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Stage',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('date_debut', models.DateField()),
                ('date_fin', models.DateField()),
                ('duree', models.DurationField()),
                ('theme', models.TextField(unique=True)),
                ('est_remunere', models.BooleanField(default=True)),
                ('evaluation', models.TextField(default='')),
                ('ecole', models.CharField(default='', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Caissier',
            fields=[
                ('personnel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='grh.personnel')),
            ],
            bases=('grh.personnel',),
        ),
        migrations.CreateModel(
            name='Infirmier',
            fields=[
                ('personnel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='grh.personnel')),
            ],
            bases=('grh.personnel',),
        ),
        migrations.CreateModel(
            name='Laborantin',
            fields=[
                ('personnel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='grh.personnel')),
            ],
            bases=('grh.personnel',),
        ),
        migrations.CreateModel(
            name='Medecin',
            fields=[
                ('personnel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='grh.personnel')),
                ('type', models.CharField(choices=[('G', 'Généraliste'), ('S', 'Spécialiste')], default='G', max_length=5)),
            ],
            bases=('grh.personnel',),
        ),
        migrations.CreateModel(
            name='Secretaire',
            fields=[
                ('personnel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='grh.personnel')),
            ],
            bases=('grh.personnel',),
        ),
        migrations.CreateModel(
            name='Stagiaire',
            fields=[
                ('personnel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='grh.personnel')),
                ('niveau', models.CharField(choices=[('BEPC', 'BEPC'), ('BAC', 'BAC'), ('BAC+1', 'BAC+1'), ('BAC+2', 'BAC+2'), ('BAC+3', 'BAC+3'), ('BAC+4', 'BAC+4'), ('BAC+5', 'BAC+5'), ('BAC+6', 'BAC+6'), ('BAC+7', 'BAC+7')], default='BAC+5', max_length=10)),
            ],
            bases=('grh.personnel',),
        ),
        migrations.CreateModel(
            name='Remuneration',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('montant', models.PositiveIntegerField()),
                ('personnel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='grh.personnel')),
            ],
        ),
        migrations.CreateModel(
            name='RapportStage',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('rapport', models.FileField(upload_to='rapports_stage/')),
                ('stage', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='grh.stage')),
            ],
        ),
    ]
