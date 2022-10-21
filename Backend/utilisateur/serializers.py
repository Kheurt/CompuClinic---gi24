from django.db.models.fields import CharField
from grh.serializers import PersonnelSerializer
from rest_framework import serializers
from django.contrib.auth.models import User, Group


class UtilisateurSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = ['url', 'id', 'username', 'password', 'personnel']
        extra_kwargs = {
            'password': {'write_only': True, 'required': False},
        }


class UtilisateurPostSerializer(serializers.ModelSerializer):
    personnel = serializers.UUIDField()
    
    class Meta:
        model = User
        exclude = ('user_permissions', 'is_active', 'date_joined', 'is_staff', 'is_superuser', 'last_login', 'email', 'first_name', 'last_name')
        extra_kwargs = {
            'password': {'write_only': True, 'required': True},
        }


class UtilisateurPutSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ('user_permissions', 'is_active', 'date_joined', 'is_staff', 'is_superuser', 'last_login', 'email', 'first_name', 'last_name', 'password')

    def get_field_names(self, declared_fields, info):
        expanded_fields = super().get_field_names(declared_fields, info)
        return expanded_fields + ['personnel']


class UtilisateurGetSerializer(serializers.ModelSerializer):
    personnel = PersonnelSerializer()
    class Meta:
        model = User
        exclude = ('password', )
    
    def get_field_names(self, declared_fields, info):
        expanded_fields = super().get_field_names(declared_fields, info)
        return ['id'] + expanded_fields


class GroupSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Group
        fields = '__all__'


class CreateUserSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=100)
    password = serializers.CharField(max_length=100)
    personnel = serializers.CharField(max_length=100)


class ProfilSerializer(serializers.ModelSerializer):
    
    
    class Meta:
        model = User
        exclude = ('password', )
        depth = 1

    def get_field_names(self, declared_fields, info):
        expanded_fields = super().get_field_names(declared_fields, info)
        return expanded_fields + ['personnel']


class UpdatePasswordSerializer(serializers.Serializer):
    password = serializers.CharField(style={'input_type': 'password'})
