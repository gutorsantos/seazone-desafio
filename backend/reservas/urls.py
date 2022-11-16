from rest_framework.routers import DefaultRouter
from reservas.views import ReservaViewSet

router = DefaultRouter()
router.register(r'anuncios', ReservaViewSet, basename='anuncios')