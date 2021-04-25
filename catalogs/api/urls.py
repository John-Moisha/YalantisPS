from catalogs.api import view
from rest_framework.routers import DefaultRouter


app_name = 'catalogs-api'

router = DefaultRouter()

router.register('categories', view.CategoryModelViewSet, basename='category')

urlpatterns = router.urls