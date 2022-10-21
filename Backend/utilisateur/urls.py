from django.urls import path, include, re_path
from rest_framework import routers

from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from compuclinic_api.settings import API_BASE_URL

from . import views


schema_view = get_schema_view(
    openapi.Info(
        title="Utilisateur API",
        default_version="v1",
        description="Documentation de l'API du module Utilisateur",
    ),
    public=True,
    url=API_BASE_URL + 'api/utilisateur-api/',
    urlconf="utilisateur.urls",
)

router = routers.DefaultRouter()
router.register('utilisateurs', views.UtilisateurViewSet)
router.register('profil', views.ProfilViewSet)
router.register('groupes', views.GroupViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('utilisateurs/<pk>/update_password', views.UpdatePasswordView.as_view()),
    
    # Swagger and Redoc UIS
    re_path(r"^swagger(?P<format>\.json|\.yaml)$", schema_view.without_ui(cache_timeout=0), name="schema-json"),
    path("swagger/", schema_view.with_ui('swagger', cache_timeout=0), name="schema-swagger-ui"),
    path("redoc/", schema_view.with_ui('redoc', cache_timeout=0), name="schema-redoc"),
]
