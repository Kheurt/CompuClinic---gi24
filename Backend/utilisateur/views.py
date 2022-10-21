from rest_framework.generics import get_object_or_404
from rest_framework.serializers import Serializer
from grh.models import Personnel
from rest_framework import exceptions, views, viewsets, mixins, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import *
from django.contrib.auth.models import User
from .serializers import *
import json

import django.contrib.auth.password_validation as validator


class UtilisateurViewSet(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.RetrieveModelMixin, mixins.CreateModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    queryset = User.objects.all()
    serializer_class = UtilisateurSerializer
    
    def get_serializer_class(self):
        if self.request.method in ['GET']:
            return UtilisateurGetSerializer
        elif self.request.method in ['PUT', 'PATCH']:
            return UtilisateurPutSerializer
        elif self.request.method in ['POST']:
            return UtilisateurPostSerializer
        else:
            return UtilisateurSerializer
    
    def create(self, request):
        print("Create User Account")
        serializer = UtilisateurPostSerializer(data=request.data)
        if serializer.is_valid():
            try:
                user = User(username=serializer.validated_data['username'])
                user.set_password(serializer.validated_data['password'])
                personnel_pk = serializer.validated_data['personnel']
                groups = serializer.validated_data['groups']
                personnel = get_object_or_404(Personnel, pk=personnel_pk)
                if personnel.user is not None:
                    return Response('Personnel already has an account!', status=status.HTTP_304_NOT_MODIFIED)
                else:
                    personnel.user = user
                    user.personnel = personnel
                    print(type(groups))
                    user.save()
                    personnel.save()
                    for group in groups:
                        user.groups.add(group)
                
                return Response({'id': user.id, **serializer.data}, status=status.HTTP_201_CREATED)
            except Exception as e:
                return Response({'error': "There is smthg fishy here..."}, status=status.HTTP_417_EXPECTATION_FAILED)

        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class ProfilViewSet(viewsets.ViewSet):
    queryset = User.objects.exclude(personnel=None)
    permission_classes = [IsAuthenticated]
    
    def list(self, request):
        serializer = ProfilSerializer(request.user)
        return Response(serializer.data)


class UpdatePasswordView(views.APIView):
    
    def post(self, request, pk):
        user = get_object_or_404(User, pk=pk)
        data = json.loads(request.body)
        print(data)
        serializer = UpdatePasswordSerializer(data=data)
        if serializer.is_valid():
            password = serializer.data['password']   
            
            """ try:
                validator.validate_password(password=password, user=user)
            except Exception as e:
                errors = {'password': list(e.messages)}
                return Response(errors, status=status.HTTP_417_EXPECTATION_FAILED) """
            
            user.set_password(password)
            user.save()

            # Update should_update_password attribute in personnel
            user.personnel.should_update_password = False
            user.personnel.save()
            return Response('Le mot de passe a bien été mis à jour!')
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)