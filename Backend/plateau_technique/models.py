from django.db import models
import uuid
from .enums import *

# TODO: Il faut bien revoir la modélisation de ce paquet, surtout concernant les relations service - unité médicale; unité médicale - local; Equipement, Materiel - Local. 

class Infrastructure(models.Model):
    """
        Une Infrastructure est une "succursale" d'une struture de santé.
    """

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nom = models.CharField(max_length=255, unique=True)
    classe = models.CharField(choices=CLASSES, max_length=2, default='C')
    image = models.ImageField(null=True, blank=True, upload_to='images/infrastructures')
    localisation = models.CharField(max_length=50)
    latitude = models.CharField(max_length=50, default="")
    longitude = models.CharField(max_length=50,default="")
    ville = models.CharField(max_length=30)
    telephone = models.CharField(max_length=30)
    fax = models.CharField(max_length=50, blank=True, null=True)
    email = models.EmailField(max_length=50, blank=True, null=True)
    site_web = models.URLField(max_length=100, blank=True, null=True)
    date_creation = models.DateField()
    date_enregistrement = models.DateTimeField(auto_now_add=True)
    directeur = models.ForeignKey('grh.Personnel', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return "Infra: " + self.nom


class InfrastructurePersonnel(models.Model):
    infrastructure = models.ForeignKey(Infrastructure, on_delete=models.SET_NULL, null=True)
    personnel = models.ForeignKey('grh.Personnel', on_delete=models.SET_NULL, null=True)
    date_embauche = models.DateField(null=True, default=None)


class PlaceParking(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    numero = models.PositiveIntegerField(unique=True)
    localisation = models.CharField(max_length=50)
    Infrastructure = models.ForeignKey(Infrastructure, on_delete=models.CASCADE)

    def __str__(self):
        return "Parking: " + self.numero


class PlaceHeliport(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    numero = models.PositiveIntegerField(unique=True)
    localisation = models.CharField(max_length=50)
    Infrastructure = models.ForeignKey(Infrastructure, on_delete=models.CASCADE)

    def __str__(self):
        return "Heliport: " + self.numero


class Batiment(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nom = models.CharField(max_length=50)
    image = models.ImageField(upload_to="images/batiments", null=True, default=None)
    surface = models.PositiveIntegerField(help_text="En mètres carré", blank=True, null=True, default=None)
    infrastructure = models.ForeignKey(Infrastructure, on_delete=models.CASCADE)
    localisation = models.CharField(max_length=50, blank=True, null=True)
    description = models.TextField(blank=True, default='')

    def __str__(self):
        return "Batiment: " + self.nom


class Local(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nom = models.CharField(max_length=50)
    image = models.ImageField(upload_to="images/locaux/", null=True, default=None)
    supericie = models.PositiveIntegerField(help_text="En mètres carré", blank=True, null=True, default=None)
    localisation = models.CharField(max_length=50, blank=True)
    batiment = models.ForeignKey(Batiment, on_delete=models.CASCADE, null=True, default=None)
    description = models.TextField(blank=True, default='')

    def __str__(self):
        return "Local: " + self.nom


# class Departement(models.Model):
#     id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)


""" class Specialite(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    type = models.CharField(choices=TYPE_UNITE, max_length=255)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    local = models.ForeignKey(Local, on_delete=models.CASCADE)
    responsable = models.ForeignKey('grh.Personnel', on_delete=models.CASCADE)

    def __str__(self):
        return "Unité Médicale: " + self.type """


class Service(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nom = models.CharField(max_length=100, default="")
    image = models.ImageField(null=True, blank=True, upload_to='images/services', default=None)
    chef = models.ForeignKey('grh.Personnel', on_delete=models.CASCADE, null=True, default=None)
    batiment = models.ForeignKey('plateau_technique.Batiment', on_delete=models.CASCADE)
    # local = models.ForeignKey('Local', on_delete=models.SET_NULL, default=None, null=True)

    def __str__(self):
        return "Service: " + self.nom


class Materiel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nom = models.CharField(max_length=50)
    image = models.ImageField(upload_to="images/materiels/", default=None, null=True)
    numero_serie = models.CharField(max_length=100, default="")
    # quantite = models.PositiveIntegerField()
    date_arrivage = models.DateTimeField(auto_now_add=True)
    local = models.ForeignKey(Local, on_delete=models.CASCADE)
    type = models.CharField(choices=TYPE_MATERIEL, default='Medical', max_length=50)

    def __str__(self):
        return "Materiel: " + self.nom


class Equipement(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    iamge = models.ImageField(upload_to="images/equipements/", default=None, null=True)
    type = models.CharField(choices=TYPE_EQUIPEMENT, max_length=255, default='Équipement d\'ambulance')
    description = models.TextField(blank=True, default='')
    local = models.ForeignKey(Local, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return "Equipement: " + self.type


class Lit(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    numero_serie = models.CharField(max_length=100, unique=True)
    image = models.ImageField(upload_to="images/lits/", default=None, null=True)
    numero = models.PositiveIntegerField(default=0)
    est_libre = models.BooleanField(default=True)
    date_enregistrement = models.DateTimeField(auto_now_add=True, editable=False)
    local = models.ForeignKey(Local, on_delete=models.SET_NULL, null=True)
