from grh.models import Personnel
from rest_framework import viewsets,views, status
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from .serializers import *
from .models import *
from grh.enums import TYPE_PERSONNEL


class EnumView(views.APIView):
    
    def get(self, request):
        param = request.query_params.get('type')
        
        # Liste des Enums
        if param is None:
            return Response(LISTE_ENUM)
        
        # Récupérer un enum
        if param in LISTE_ENUM.keys():
            res = LISTE_ENUM[param]
            return Response(res)
        else:
            return Response({'error': 'Pas d\'enum de ce type'}, status=status.HTTP_400_BAD_REQUEST)


class InfrastructureViewSet(viewsets.ModelViewSet):
    queryset = Infrastructure.objects.all().order_by('nom')
    serializer_class = InfrastructureSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['nom', 'ville', 'localisation']
    
    def get_serializer_class(self):
        if self.request.method in ['GET']:
            return InfrastructureNestedSerializer
        else:
            return InfrastructureSerializer


class InfrastructurePersonnelViewSet(viewsets.ModelViewSet):
    queryset = InfrastructurePersonnel.objects.all()
    serializer_class = InfrastructurePersonnelCreateSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['infrastructure', 'personnel']
    
    def get_serializer_class(self):
        if self.request.method in ['GET']:
            return InfrastructurePersonnelNestedSerializer
        else:
            return InfrastructurePersonnelCreateSerializer


class PersonnelInfrastructureCountView(views.APIView):
    
    def get(self, request, pk):
        infrastructure = get_object_or_404(Infrastructure, pk=pk)
        personnels_infra = infrastructure.infrastructurepersonnel_set.all()

        result = {}
        for entry in TYPE_PERSONNEL:
            val, label = entry
            count = personnels_infra.filter(personnel__type_personnel=val).count()
            result[label] = count
        
        return Response(result)


class ServicesInfrastructureView(views.APIView):
    
    def  get(self, request, pk):
        # Récupérer la liste des services par infrastructure dans la BD
        infrastructure = get_object_or_404(Infrastructure, pk=pk)
        batiments = infrastructure.batiment_set.all()
        services = Service.objects.filter(batiment__in=batiments)
        
        # Serializer et Afficher les résultats de recherche
        serializer = ServiceNestedSerializer(services, many=True)
        return Response(serializer.data)


class ServicesInfrastructureCountView(views.APIView):
    
    def get(self, request, pk):
        # Récupérer le nombre des services par infrastructure dans la BD
        infrastructure = get_object_or_404(Infrastructure, pk=pk)
        batiments = infrastructure.batiment_set.all()
        nbr = Service.objects.filter(batiment__in=batiments).count()

        return Response({'total': nbr})


class PlaceParkingViewSet(viewsets.ModelViewSet):
    queryset = PlaceParking.objects.all()
    serializer_class = PlaceParkingSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['localisation', 'numero']

    def get_serializer_class(self):
        if self.request.method in ['GET']:
            return PlaceParkingNestedSerializer
        else:
            return PlaceParkingSerializer

class PlaceParkingInfrastructureCountView(views.APIView):
    
    def get(self, request, pk):
        # Récupérer le nombre des services par infrastructure dans la BD
        infrastructure = get_object_or_404(Infrastructure, pk=pk)
        nbr = infrastructure.placeparking_set.count()

        return Response({'total': nbr})

class PlaceHeliportViewSet(viewsets.ModelViewSet):
    queryset = PlaceHeliport.objects.all()
    serializer_class = PlaceHeliportSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['localisation', 'numero']
    
    def get_serializer_class(self):
        if self.request.method in ['GET']:
            return PlaceHeliportNestedSerializer
        else:
            return PlaceHeliportSerializer


class BatimentViewSet(viewsets.ModelViewSet):
    queryset = Batiment.objects.all()
    serializer_class = BatimentSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['nom']
    
    def get_serializer_class(self):
        if self.request.method in ['GET']:
            return BatimentNestedSerializer
        else:
            return BatimentSerializer


class BatimentsInfrastructureCountView(views.APIView):
    
    def get(self, request, pk):
        # Récupérer le nombre des services par infrastructure dans la BD
        infrastructure = get_object_or_404(Infrastructure, pk=pk)
        nbr = infrastructure.batiment_set.count()

        return Response({'total': nbr})


class LocalViewSet(viewsets.ModelViewSet):
    queryset = Local.objects.all()
    serializer_class = LocalSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['batiment']
    
    def get_serializer_class(self):
        if self.request.method in ['GET']:
            return LocalNestedSerializer
        else:
            return LocalSerializer


class LocauxInfrastructureCountView(views.APIView):
    
    def get(self, request, pk):
        # Récupérer le nombre des services par infrastructure dans la BD
        infrastructure = get_object_or_404(Infrastructure, pk=pk)
        batiments = infrastructure.batiment_set.all()
        nbr = Local.objects.filter(batiment__in=batiments).count()

        return Response({'total': nbr})


class ServiceViewSet(viewsets.ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['chef', 'nom', 'batiment']
    search_fields = ['nom']
    
    def get_serializer_class(self):
        if self.request.method in ['GET']:
            return ServiceNestedSerializer
        else:
            return ServiceSerializer


""" class UniteMedicaleViewSet(viewsets.ModelViewSet):
    queryset = UniteMedicale.objects.all()
    serializer_class = UniteMedicaleSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = [] """


class EquipementViewSet(viewsets.ModelViewSet):
    queryset = Equipement.objects.all()
    serializer_class = EquipementSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['local', 'type']
    search_fields = ['type']
    
    def get_serializer_class(self):
        if self.request.method in ['GET']:
            return EquipementNestedSerializer
        else:
            return EquipementSerializer


class EquipementsInfrastructureCountView(views.APIView):
    
    def get(self, request, pk):
        # Récupérer le nombre des services par infrastructure dans la BD
        infrastructure = get_object_or_404(Infrastructure, pk=pk)
        batiments = infrastructure.batiment_set.all()
        locaux = Local.objects.filter(batiment__in=batiments)
        equipements = Equipement.objects.filter(local__in=locaux)
        
        # Décompte des équipements par type
        result =  {}
        
        # On récupère d'abord la liste des types d'equipements : .enums.TYPE_EQUIPEMENT
        # Pour chaque type d'équipements, on fait le décompte et on ajoute dans le résultat. Si le décompte est null, on ne prends pas en compte
        for type_eq in TYPE_EQUIPEMENT:
            val = type_eq[0]
            label = type_eq[1]
            count = equipements.filter(type=val).count()
            result[label] = count

        return Response(result)


class MaterielsInfrastructureCountView(views.APIView):
    
    def get(self, request, pk):
        # Récupérer le nombre des services par infrastructure dans la BD
        infrastructure = get_object_or_404(Infrastructure, pk=pk)
        batiments = infrastructure.batiment_set.all()
        locaux = Local.objects.filter(batiment__in=batiments)
        materiels = Materiel.objects.filter(local__in=locaux)
        
        # Décompte des équipements par type
        result =  {}
        
        # On récupère d'abord la liste des types d'equipements : .enums.TYPE_EQUIPEMENT
        # Pour chaque type d'équipements, on fait le décompte et on ajoute dans le résultat. Si le décompte est null, on ne prends pas en compte
        for type_eq in TYPE_MATERIEL:
            val = type_eq[0]
            label = type_eq[1]
            count = materiels.filter(type=val).count()
            result[label] = count

        return Response(result)

class ComposantsInfrastructureCountView(views.APIView):
    
    def get(self, request, pk):
        infrastructure = get_object_or_404(Infrastructure, pk=pk)
        batiments = infrastructure.batiment_set.all()
        locaux = Local.objects.filter(batiment__in=batiments)
        materiels = Materiel.objects.filter(local__in=locaux)
        placeparking = infrastructure.placeparking_set.all()
        placeheliport = infrastructure.placeheliport_set.all()
        equipements = Equipement.objects.filter(local__in=locaux)
        services = Service.objects.filter(batiment__in=batiments)
        personnels_infra = infrastructure.infrastructurepersonnel_set.all()

        result_pers = {}
        for entry in TYPE_PERSONNEL:
            val, label = entry
            count = personnels_infra.filter(personnel__type_personnel=val).count()
            result_pers[label] = count
        
        result_materiel = {}
        for type_eq in TYPE_MATERIEL:
            val = type_eq[0]
            label = type_eq[1]
            count = materiels.filter(type=val).count()
            result_materiel[label] = count

        
        result_equ =  {}
        for type_eq in TYPE_EQUIPEMENT:
            val = type_eq[0]
            label = type_eq[1]
            count = equipements.filter(type=val).count()
            result_equ[label] = count
        
        
        result = {}
        result['batiments'] = batiments.count()
        result['locaux'] = locaux.count()
        result['places_parking'] = placeparking.count()
        result['places_heliport'] = placeheliport.count()
        result['services'] = services.count()
        result['materiels'] = result_materiel
        result['equipements'] = result_equ
        result['personnel'] = result_pers

        return Response(result)


class MaterielViewSet(viewsets.ModelViewSet):
    queryset = Materiel.objects.all()
    serializer_class = MaterielSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['local', 'type', 'nom']
    search_fields = ['nom', 'type']

    def get_serializer_class(self):
        if self.request.method in ['GET']:
            return MaterielNestedSerializer
        else:
            return MaterielSerializer


class LitViewSet(viewsets.ModelViewSet):
    queryset = Lit.objects.all()
    serializer_class = LitSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['local', 'est_libre']
    
    def get_serializer_class(self):
        if self.request.method in ['GET']:
            return LitNestedSerializer
        else:
            return LitSerializer
