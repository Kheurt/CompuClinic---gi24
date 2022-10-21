import consultation
from grh.models import Laborantin
from .models import *
from rest_framework import serializers
from plateau_technique.serializers import ServiceSerializer
from grh.serializers import LaborantinNestedSerializer, MedecinSerializer, PersonnelSerializer, LaborantinSerializer
from secretariat.serializers import DossierNestedSerializer


class ConsultationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Consultation
        fields = '__all__'
        read_only_fields = [
            'id',
            'date_creation',
        ]
        extra_kwargs = {
            'precedant': {
                'allow_null': True,
                'required': False,
            },
        }
    
    # Adding extra fields (id)
    def get_field_names(self, declared_fields, info):
        expanded_fields = super().get_field_names(declared_fields, info)
        return expanded_fields + ['id']


class  BulletinExamenSerializer(serializers.ModelSerializer):
    class Meta:
        model = BulletinExamen
        fields = '__all__'
        read_only_fields = [
            'id',
            'date_creation',
        ]
        extra_kwargs = {
            'precedant': {
                'allow_null': True,
                'required': False,
            },
        }
      
          # Adding extra fields (id)
    def get_field_names(self, declared_fields, info):
        expanded_fields = super().get_field_names(declared_fields, info)
        return expanded_fields + ['id']

class  BulletinExamenNestedSerializer(serializers.ModelSerializer):
        
      class Meta:
        model = BulletinExamen
        fields = '__all__'
        read_only_fields = [
            'id',
            'date_creation',
        ]
        extra_kwargs = {
            'precedant': {
                'allow_null': True,
                'required': False,
            },
        }

class ConsultationNestedSerializer(serializers.ModelSerializer):
    service = ServiceSerializer()
    medecin = MedecinSerializer()
    dossier = DossierNestedSerializer()
    
    class Meta:
        model = Consultation
        fields = '__all__'
        read_only_fields = [
            'id',
            'date_creation',
        ]
        extra_kwargs = {
            'precedant': {
                'allow_null': True,
                'required': False,
            },
        }
    
    # Adding extra fields (id)
    def get_field_names(self, declared_fields, info):
        expanded_fields = super().get_field_names(declared_fields, info)
        return expanded_fields + ['id']


class ParametreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Parametre
        fields = '__all__'
        read_only_fields = [
            'id',
            'date_creation',
        ]
        extra_kwargs = {
            'commentaire': {
                'default': '',
                'required': False
            }
        }
    
    # Adding extra fields (id)
    def get_field_names(self, declared_fields, info):
        expanded_fields = super().get_field_names(declared_fields, info)
        return expanded_fields + ['id']


class ParametreNestedSerializer(serializers.ModelSerializer):
    auteur = PersonnelSerializer()
    
    class Meta:
        model = Parametre
        fields = '__all__'
        read_only_fields = [
            'id',
            'date_creation',
        ]
        extra_kwargs = {
            'commentaire': {
                'default': '',
                'required': False
            }
        }
    
    # Adding extra fields (id)
    def get_field_names(self, declared_fields, info):
        expanded_fields = super().get_field_names(declared_fields, info)
        return expanded_fields + ['id']


class SymptomeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Symptome
        fields = '__all__'
        read_only_fields = [
            'id',
        ]
    
    # Adding extra fields (id)
    def get_field_names(self, declared_fields, info):
        expanded_fields = super().get_field_names(declared_fields, info)
        return expanded_fields + ['id']


class DifferentielSerializer(serializers.ModelSerializer):
    class Meta:
        model = Differentiel
        fields = '__all__'
        read_only_fields = [
            'id',
        ]
        extra_kwargs = {
            'justificatif': {
                'default': '',
                'required': False
            }
        }
    
    # Adding extra fields (id)
    def get_field_names(self, declared_fields, info):
        expanded_fields = super().get_field_names(declared_fields, info)
        return expanded_fields + ['id']


class PrescriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prescription
        fields = '__all__'
        read_only_fields = [
            'id',
            'date_creation'
        ]
    
    # Adding extra fields (id)
    def get_field_names(self, declared_fields, info):
        expanded_fields = super().get_field_names(declared_fields, info)
        return expanded_fields + ['id']


class RecommandationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recommandation
        fields = '__all__'
        read_only_fields = [
            'id',
            'date_creation'
        ]
    
    # Adding extra fields (id)
    def get_field_names(self, declared_fields, info):
        expanded_fields = super().get_field_names(declared_fields, info)
        return expanded_fields + ['id']


class PrescriptionMedicamenteuseSerializer(serializers.ModelSerializer):
    class Meta:
        model = PrescriptionMedicamenteuse
        fields = '__all__'
        read_only_fields = [
            'id',
            'date_creation'
        ]
    
    # Adding extra fields (id)
    def get_field_names(self, declared_fields, info):
        expanded_fields = super().get_field_names(declared_fields, info)
        return expanded_fields + ['id']


class PrescriptionExamenSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = PrescriptionExamen
        fields = '__all__'
        read_only_fields = [
            'id',
            'date_creation',
        ]
    
    # Adding extra fields (id)
    def get_field_names(self, declared_fields, info):
        expanded_fields = super().get_field_names(declared_fields, info)
        return expanded_fields + ['id']


class ExamenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Examen
        fields = '__all__'
        read_only_fields = [
            'id',
            'date_creation',
        ]
        extra_kwargs = {
            'resultat': {
                'required': False
            },
            'prescription': {
                'allow_null': True,
                'required': False
            }
        }
        
    # Adding extra fields (id)
    def get_field_names(self, declared_fields, info):
        expanded_fields = super().get_field_names(declared_fields, info)
        return expanded_fields + ['id']

class ExamenNestedSerializer(serializers.ModelSerializer):
    laborantin = LaborantinNestedSerializer()
    consultation = ConsultationNestedSerializer()
    prescription = PrescriptionExamenSerializer()

    class Meta:
        model = Examen
        fields = '__all__'
        read_only_fields = [
            'id',
            'date_creation',
        ]
        extra_kwargs = {
            'resultat': {
                'required': False
            },
            'prescription': {
                'allow_null': True,
                'required': False
            }
        }
        
    # Adding extra fields (id)
    def get_field_names(self, declared_fields, info):
        expanded_fields = super().get_field_names(declared_fields, info)
        return ['id'] + expanded_fields


class TestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Test
        fields = '__all__'
        read_only_fields = ['id']
    
    # Adding extra fields (id)
    def get_field_names(self, declared_fields, info):
        expanded_fields = super().get_field_names(declared_fields, info)
        return expanded_fields + ['id']
