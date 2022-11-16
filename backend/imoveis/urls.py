from rest_framework.routers import DefaultRouter
from imoveis.views import ImovelViewSet

router = DefaultRouter()
router.register(r'imoveis', ImovelViewSet, basename='imoveis')