from rest_framework.routers import DefaultRouter
from anuncios.views import AnuncioViewSet

router = DefaultRouter()
router.register(r'anuncios', AnuncioViewSet, basename='anuncios')