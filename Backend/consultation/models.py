from django.db import models
import uuid
from caisse.models import TIAPS
from caisse.models import Quittance
from .enum import *
from datetime import timedelta
from datetime import datetime as dtm


class Consultation(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    date_creation = models.DateTimeField(auto_now_add=True)
    type = models.PositiveIntegerField(choices=TYPE, default=0)
    service = models.ForeignKey('plateau_technique.Service', on_delete=models.CASCADE)
    dossier = models.ForeignKey('secretariat.Dossier', on_delete=models.CASCADE)
    medecin = models.ForeignKey('grh.Medecin', on_delete=models.SET_NULL, null=True)
    precedant = models.ForeignKey('Consultation', on_delete=models.CASCADE, null=True)
    en_cours = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        print(self.dossier.patient)
        
        if self.date_creation is None:
            if TIAPS.utiliser(self.dossier.patient):
                super().save(*args, **kwargs)
            else:
                raise Exception("Non Used TIAPS for this User Does not existst!")
        else:
            super().save(*args, **kwargs)
    
    def fermer(self):
        self.en_cours = False
        self.save()

class Parametre(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    type = models.CharField(choices=TYPES_PARAMETRE, max_length=20)
    valeur = models.DecimalField(decimal_places=2, max_digits=6)
    commentaire = models.TextField(blank=True)
    auteur = models.ForeignKey('grh.Personnel', on_delete=models.SET_NULL, null=True)
    # TODO: Vérfier que seul le personnel autorisé peut prendre un paramètre
    date_prise = models.DateTimeField(auto_now_add=True, editable=False)
    consultation = models.ForeignKey('Consultation', on_delete=models.CASCADE)

class BulletinExamen(models.Model):
    # examen_ptr_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    qExam_Buy = models.BooleanField(default=False)
    laborantin = models.ForeignKey('grh.Laborantin', on_delete=models.CASCADE)  
    consultation  = models.ForeignKey("Consultation", on_delete=models.CASCADE)
    date_prelevement = models.DateTimeField(auto_now=True)
    resultat = models.CharField(choices=RESULTAT_COVID,max_length=30,default=RESULTAT_COVID[0])
    Conclusion = models.CharField(max_length=200, null=True)
    prescription = models.ForeignKey('PrescriptionExamen', on_delete=models.SET_NULL, null=True)
    globuleRouge = models.CharField(max_length=50 ,  null=True)
    globuleBlanc = models.CharField(max_length=50,  null=True)
    tauxHemoglobines= models.CharField(max_length=50,  null=True)
    hematocritie = models.CharField(max_length=50,  null=True)
    vgm = models.CharField(max_length=50, null=True)
    plaquettes = models.CharField(max_length=50 ,  null=True)
    neutrophiles = models.CharField(max_length=50,  null=True)
    eosinophiles = models.CharField(max_length=50,  null=True)
    basophile = models.CharField(max_length=50,  null=True)
    lymphocytes = models.CharField(max_length=50, null=True)
    monocytes = models.CharField(max_length=50,  null=True)
    electroPhoreseHb = models.CharField(max_length=50,  null=True)
    tp = models.CharField(max_length=50,  null=True)
    tck= models.CharField(max_length=50,  null=True)
    vs = models.CharField(max_length=50,  null=True)
    groupeSanguin = models.CharField(max_length=50, null=True)
    gouttesEpaisse = models.CharField(max_length=50, null=True)
    testEmmel = models.CharField(max_length=50, null=True)
    rmf = models.CharField(max_length=50, null=True)
    sniptest = models.CharField(max_length=50,  null=True)
    vih = models.CharField(max_length=50,  null=True)
    aslo = models.CharField(max_length=50,  null=True)
    crp = models.CharField(max_length=50,  null=True)
    tpha = models.CharField(max_length=50, null=True)
    vdrl = models.CharField(max_length=50,  null=True)
    aghbs = models.CharField(max_length=50,  null=True)
    achcv = models.CharField(max_length=50, null=True)
    toxoplasmose = models.CharField(max_length=50,  null=True)
    chlamydiale = models.CharField(max_length=50, null=True)
    rubeole = models.CharField(max_length=50,  null=True)
    widalTest = models.CharField(max_length=50, null=True)
    facteursRhumatoides = models.CharField(max_length=50, null=True)
    hpylori = models.CharField(max_length=50, null=True)
    sang = models.CharField(max_length=50, null=True)
    uree = models.CharField(max_length=50,  null=True)
    creatinine = models.CharField(max_length=50, null=True)
    asat = models.CharField(max_length=50, null=True)
    alat = models.CharField(max_length=50, null=True)
    acideUrique = models.CharField(max_length=50, null=True)
    glecemieAjeun = models.CharField(max_length=50, null=True)
    pal = models.CharField(max_length=50, null=True)
    triglycerides = models.CharField(max_length=50,  null=True)
    cholesterolT = models.CharField(max_length=50,  null=True)
    hdlcholesterol = models.CharField(max_length=50, null=True)
    hdglyque = models.CharField(max_length=50, null=True)
    soduim = models.CharField(max_length=50,  null=True)
    potassium = models.CharField(max_length=50,  null=True)
    chlore = models.CharField(max_length=50,  null=True)
    calcium = models.CharField(max_length=50,  null=True)
    magnesium = models.CharField(max_length=50,null=True)
    urines = models.CharField(max_length=50,  null=True)
    lcr = models.CharField(max_length=50,  null=True)
    proteine= models.CharField(max_length=50,  null=True)
    glucose = models.CharField(max_length=50,  null=True)
    densite = models.CharField(max_length=50,  null=True)
    leucocytes = models.CharField(max_length=50,  null=True)
    acideAscorbique = models.CharField(max_length=50,  null=True)
    nitrites = models.CharField(max_length=50,  null=True)
    coprscetonique = models.CharField(max_length=50,  null=True)
    urobilinogene = models.CharField(max_length=50,  null=True)
    biluribine = models.CharField(max_length=50,  null=True)
    selbilaires = models.CharField(max_length=50,  null=True)
    ph = models.CharField(max_length=50,  null=True)
    hcg = models.CharField(max_length=50,  null=True)
    selles = models.CharField(max_length=50,  null=True)
    mycoplasme = models.CharField(max_length=50, null=True)

class Symptome(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nom = models.CharField(max_length=50, default="")
    description = models.TextField()
    # duree = models.DurationField(blank=True, default='')
    type_symptome = models.CharField(max_length=5, choices=TYPES_SYMPTOME, default="A")
    frequence = models.CharField(blank=True, max_length=100, default='')
    intensité = models.CharField(blank=True, max_length=100, default='')
    localisation = models.CharField(blank=True, max_length=100, default='')
    consultation = models.ForeignKey('Consultation', on_delete=models.CASCADE)


class Differentiel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    maladie = models.CharField(max_length=255)
    justificatif = models.TextField(blank=True)
    consultation = models.ForeignKey('Consultation', on_delete=models.CASCADE)


class Prescription(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    date_creation = models.DateTimeField(auto_now_add=True, editable=False)
    consultation = models.ForeignKey('Consultation', on_delete=models.CASCADE)


class Recommandation(Prescription):
    label = models.CharField(max_length=100, default="" ,null=True)
    description = models.TextField()


class PrescriptionMedicamenteuse(Prescription):
    medicament = models.CharField(max_length=50)
    dose = models.CharField(max_length=50)
    frequence = models.CharField(max_length=50)
    duree = models.CharField(max_length=100)
    description = models.TextField(default="")


class PrescriptionExamen(Prescription):
    ETAT = (
        ('PAYE', 'Payé'),
        ('FAIT', 'Fait')
    )
    # label = models.CharField(default="", max_length=150 ,null=True)
    description = models.TextField(default="")
    type = models.CharField(max_length=2000, default="")
    est_fait = models.BooleanField(default=False)
    nom = models.CharField(max_length=100 , null=True)


class Examen(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nom = models.CharField(max_length=100 , null=True)
    type = models.CharField(max_length=2000, default="")
    date_creation = models.DateTimeField(auto_now_add=True, editable=False)
    resultat = models.TextField(blank=True, default='')
    laborantin = models.ForeignKey('grh.Laborantin', on_delete=models.CASCADE)
    est_fait = models.BooleanField(default=False)
    consultation  = models.ForeignKey("Consultation", on_delete=models.CASCADE)
    est_sur_prescription = models.BooleanField(default=True)
    prescription = models.ForeignKey('PrescriptionExamen', on_delete=models.SET_NULL, null=True)


# class CreationTest(models.Model):
#     id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
#     prescription = models.ForeignKey('PrescriptionExamen', on_delete=models.SET_NULL, null=True)
#     listepresence = models.ForeignKey(Quittance, on_delete=models.CASCADE)

class Test(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nom = models.CharField(max_length=50)
    resultat = models.CharField(max_length=50)
    examen = models.ForeignKey(Quittance, on_delete=models.CASCADE)
