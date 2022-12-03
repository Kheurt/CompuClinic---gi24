from django.urls import path, include, re_path
from rest_framework import routers

from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from compuclinic_api.settings import API_BASE_URL

from . import views


schema_view = get_schema_view(
    openapi.Info(
        title="Secretariat API",
        default_version="v1",
        description="Documentation de l'API du module Secretariat",
    ),
    public=True,
    url=API_BASE_URL  + 'api/secretariat-api/',
    urlconf="secretariat.urls",
)


router = routers.DefaultRouter()
router.register('patients', views.PatientViewSet)
router.register('dossiers', views.DossierViewSet)
router.register('liste-presence', views.ListePresenceViewSet)
router.register('internements', views.InternementViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('patients/<pk>/interner-patient/', views.InternerPatient.as_view()),
    path('patients/<pk>/externer-patient/', views.ExternerPatient.as_view()),
    path('patients/<pk>/quittances/', views.ListeQuittanceView.as_view()),
    path('patients/<pk>/bons/', views.ListeBonView.as_view()),
    path('secretariat/<pk>/data-you', views.GeneratePdf.as_view()),
    path('enums/', views.EnumView.as_view()),
    
    # Swagger and Redoc UIS
    re_path(r"^swagger(?P<format>\.json|\.yaml)$", schema_view.without_ui(cache_timeout=0), name="schema-json"),
    path("swagger/", schema_view.with_ui('swagger', cache_timeout=0), name="schema-swagger-ui"),
    path("redoc/", schema_view.with_ui('redoc', cache_timeout=0), name="schema-redoc"),
]
