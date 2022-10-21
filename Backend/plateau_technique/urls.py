from django.urls import path, include, re_path
from rest_framework import routers

from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from compuclinic_api.settings import API_BASE_URL

from . import views


schema_view = get_schema_view(
    openapi.Info(
        title="Plateau Technique API",
        default_version="v1",
        description="Documentation de l'API du module Plateau Technique",
    ),
    public=True,
    url=API_BASE_URL + 'api/plateau-technique-api/',
    urlconf="plateau_technique.urls",
)

router = routers.DefaultRouter()
router.register('infrastructures', views.InfrastructureViewSet)
router.register('places-parking', views.PlaceParkingViewSet)
router.register('places-heliport', views.PlaceHeliportViewSet)
router.register('batiments', views.BatimentViewSet)
router.register('locaux', views.LocalViewSet)
# router.register('unites-medicales', views.UniteMedicaleViewSet)
router.register('equipements', views.EquipementViewSet)
router.register('materiels', views.MaterielViewSet)
router.register('lits', views.LitViewSet)
router.register('services', views.ServiceViewSet)
router.register('personnels-infrastructures', views.InfrastructurePersonnelViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('enums/', views.EnumView.as_view()),
    path('infrastructures/<pk>/services/', views.ServicesInfrastructureView.as_view()),
    path('infrastructures/<pk>/services/count/', views.ServicesInfrastructureCountView.as_view()),
    path('infrastructures/<pk>/batiments/count/', views.BatimentsInfrastructureCountView.as_view()),
    path('infrastructures/<pk>/places-parking/count/', views.PlaceParkingInfrastructureCountView.as_view()),
    path('infrastructures/<pk>/locaux/count/', views.LocauxInfrastructureCountView.as_view()),
    path('infrastructures/<pk>/equipements/count/', views.EquipementsInfrastructureCountView.as_view()),
    path('infrastructures/<pk>/materiels/count/', views.MaterielsInfrastructureCountView.as_view()),
    path('infrastructures/<pk>/composants/count/', views.ComposantsInfrastructureCountView.as_view()),
    path('infrastructures/<pk>/personnel/count/', views.PersonnelInfrastructureCountView.as_view()),
    
    # Swagger and Redoc UIS
    re_path(r"^swagger(?P<format>\.json|\.yaml)$", schema_view.without_ui(cache_timeout=0), name="schema-json"),
    path("swagger/", schema_view.with_ui('swagger', cache_timeout=0), name="schema-swagger-ui"),
    path("redoc/", schema_view.with_ui('redoc', cache_timeout=0), name="schema-redoc"),
]
