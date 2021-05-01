from catalogs.api import views
from rest_framework.routers import DefaultRouter


app_name = 'catalogs-api'

router = DefaultRouter()

router.register('courses', views.CourseModelViewSet, basename='course')
router.register('catalogs', views.CatalogModelViewSet, basename='catalog')
urlpatterns = router.urls
