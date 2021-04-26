from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from catalogs.api.filters import CatalogFilter, CourseFilter
from catalogs.api.serializers import CatalogSerializer, CourseSerializer
from catalogs.models import Catalog, Course


class CatalogModelViewSet(viewsets.ModelViewSet):
    queryset = Catalog.objects.all()
    serializer_class = CatalogSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    ordering_fields = ['title_category']
    filterset_class = CatalogFilter


class CourseModelViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    ordering_fields = ['title_course', 'date_start', 'date_end', 'quantity']
    filterset_class = CourseFilter
