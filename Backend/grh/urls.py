from django.urls import path, include, re_path
from rest_framework import routers

from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from compuclinic_api.settings import API_BASE_URL

from . import views


schema_view = get_schema_view(
    openapi.Info(
        title="GRH API",
        default_version="v1",
        description="Documentation de l'API du module GRH",
    ),
    public=True,
    url=API_BASE_URL + 'api/grh-api/',
    urlconf="grh.urls",
)


router = routers.DefaultRouter()
router.register('periodes', views.PeriodeViewSet)
router.register('postes', views.PosteViewSet)
router.register('infirmiers', views.InfirmierViewSet)
router.register('secretaires', views.SecretaireViewSet)
router.register('caissiers', views.CaissierViewSet)
router.register('laborantins', views.LaborantinViewSet)
router.register('medecins', views.MedecinViewSet)
router.register('profils-specialiste', views.ProfilSpecialisteViewSet)
router.register('stagiaires', views.StagiaireViewSet)
router.register('stages', views.StageViewSet)
router.register('rapports-stage', views.RapportStageViewSet)
router.register('permissions', views.PermissionViewSet)
router.register('absences', views.AbsenceViewSet)
router.register('pointages', views.PointageViewSet)
router.register('remunerations', views.RemunerationViewSet)
router.register('personnels', views.PersonnelViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('emploi_de_temps/', views.EmploiDeTempsView.as_view()),
    path('enums/', views.EnumView.as_view()),
    
    # Swagger and Redoc UIS
    re_path(r"^swagger(?P<format>\.json|\.yaml)$", schema_view.without_ui(cache_timeout=0), name="schema-json"),
    path("swagger/", schema_view.with_ui('swagger', cache_timeout=0), name="schema-swagger-ui"),
    path("redoc/", schema_view.with_ui('redoc', cache_timeout=0), name="schema-redoc"),
]
