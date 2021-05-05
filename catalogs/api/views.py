from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from catalogs.api.filters import CourseFilter
from catalogs.api.serializers import CourseSerializer, CatalogSerializer
from catalogs.models import Course, Catalog


class CourseModelViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['title_course', 'date_start', 'date_end', 'quantity']
    filterset_class = CourseFilter
    search_fields = ['title_course']


class CatalogModelViewSet(viewsets.ModelViewSet):
    queryset = Catalog.objects.all()
    serializer_class = CatalogSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    ordering_fields = ['title_catalog']
