from catalogs.api import views
from rest_framework.routers import DefaultRouter


app_name = 'catalogs-api'

router = DefaultRouter()

router.register('courses', views.CourseModelViewSet, basename='course')

urlpatterns = router.urls
