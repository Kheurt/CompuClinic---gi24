from .models import *
from rest_framework import serializers
from grh.serializers import PersonnelSerializer

class InfrastructureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Infrastructure
        fields = '__all__'
        read_only_fields = ['id', 'date_enregistrement']
        extra_kwargs = {
            'image': {
                'required': False
            },
            'fax': {
                'default': ''
            },
            'email': {
                'default': ''
            },
            'site_web': {
                'default': ''
            }
        }
    
    # Adding extra fields (id)
    def get_field_names(self, declared_fields, info):
        expanded_fields = super().get_field_names(declared_fields, info)
        return expanded_fields + ['id']


class InfrastructureNestedSerializer(serializers.ModelSerializer):
    directeur = PersonnelSerializer()
    
    class Meta:
        model = Infrastructure
        fields = '__all__'


class InfrastructurePersonnelNestedSerializer(serializers.ModelSerializer):
    personnel = PersonnelSerializer()
    
    class Meta:
        model = InfrastructurePersonnel
        fields = '__all__'

class InfrastructurePersonnelCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = InfrastructurePersonnel
        fields  = '__all__'


class PlaceParkingSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlaceParking
        fields = '__all__'
        read_only_fields = ['id']
        
    # Adding extra fields (id)
    def get_field_names(self, declared_fields, info):
        expanded_fields = super().get_field_names(declared_fields, info)
        return expanded_fields + ['id']


class PlaceParkingNestedSerializer(serializers.ModelSerializer):
    infrastructure = InfrastructureSerializer()
    
    class Meta:
        model = PlaceParking
        fields = '__all__'


class PlaceHeliportSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlaceHeliport
        fields = '__all__'
        read_only_fields = ['id']
        
    # Adding extra fields (id)
    def get_field_names(self, declared_fields, info):
        expanded_fields = super().get_field_names(declared_fields, info)
        return expanded_fields + ['id']


class PlaceHeliportNestedSerializer(serializers.ModelSerializer):
    infrastructure = InfrastructureSerializer()
    
    class Meta:
        model = PlaceHeliport
        fields = '__all__'


class BatimentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Batiment
        fields = '__all__'
        read_only_fields = ['id']
        
    # Adding extra fields (id)
    def get_field_names(self, declared_fields, info):
        expanded_fields = super().get_field_names(declared_fields, info)
        return expanded_fields + ['id']


class BatimentNestedSerializer(serializers.ModelSerializer):
    infrastructure = InfrastructureSerializer()
    
    class Meta:
        model = Batiment
        fields = '__all__'


class LocalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Local
        fields = '__all__'
        read_only_fields = ['id']
    
    # Adding extra fields (id)
    def get_field_names(self, declared_fields, info):
        expanded_fields = super().get_field_names(declared_fields, info)
        return expanded_fields + ['id']


class LocalNestedSerializer(serializers.ModelSerializer):
    batiment = BatimentSerializer()
    
    class Meta:
        model = Local
        fields = '__all__'


""" class UniteMedicaleSerializer(serializers.ModelSerializer):
    class Meta:
        model = UniteMedicale
        fields = '__all__'
        read_only_fields = ['id']
    
    # Adding extra fields (id)
    def get_field_names(self, declared_fields, info):
        expanded_fields = super().get_field_names(declared_fields, info)
        return expanded_fields + ['id'] """


class MaterielSerializer(serializers.ModelSerializer):
    class Meta:
        model = Materiel
        fields = '__all__'
        read_only_fields = ['id']
    
    # Adding extra fields (id)
    def get_field_names(self, declared_fields, info):
        expanded_fields = super().get_field_names(declared_fields, info)
        return expanded_fields + ['id']


class MaterielNestedSerializer(serializers.ModelSerializer):
    local = LocalSerializer()
    
    class Meta:
        model = Materiel
        fields = '__all__'


class EquipementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Equipement
        fields = '__all__'
        read_only_fields = ['id']
    
    # Adding extra fields (id)
    def get_field_names(self, declared_fields, info):
        expanded_fields = super().get_field_names(declared_fields, info)
        return expanded_fields + ['id']


class EquipementNestedSerializer(serializers.ModelSerializer):
    local = LocalNestedSerializer()
    
    class Meta:
        model = Equipement
        fields = '__all__'


class LitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lit
        fields  = '__all__'
        read_only_fields = ['est_libre']
        extra_kwargs = {
            'numero': {'required': True}
        }


class LitNestedSerializer(serializers.ModelSerializer):
    local = LocalNestedSerializer()
    
    class Meta:
        model = Lit
        fields = '__all__'


class ServiceSerializer(serializers.ModelSerializer):
    # TODO Il faut redéfinir le champ chef pour utiliser le bon sérializer en fonction du type de personnel
    # Ou encore on définit une fois une vues spécialisée pour le type Personnel
    # TODO Voir aussi le cas de caisse.Bon
    class Meta:
        model = Service
        fields = '__all__'
        read_only_fields = ['id']
        extra_kwargs = {
            'nom': {'required': True},
        }

    # Adding extra fields (id)
    def get_field_names(self, declared_fields, info):
        expanded_fields = super().get_field_names(declared_fields, info)
        return expanded_fields + ['id']

class ServiceNestedSerializer(serializers.ModelSerializer):
    chef = PersonnelSerializer()
    batiment = BatimentSerializer()
    
    class Meta:
        model = Service
        fields = '__all__'
