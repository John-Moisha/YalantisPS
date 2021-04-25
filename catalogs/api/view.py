from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from catalogs.api.filters import CategoryFilter, CourseFilter
from catalogs.api.serializers import CategorySerializer, CourseSerializer
from catalogs.models import Category, Course


class CategoryModelViewSet(viewsets.ModelViewSet):
    queryset = Category.object.all()
    serializer_class = CategorySerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    ordering_fields = ['title_category']
    filterset_class = CategoryFilter


class CourseModelViewSet(viewsets.ModelViewSet):
    queryset = Course.object.all()
    serializer_class = CourseSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    ordering_fields = ['title_course', 'date_start', 'date_end', 'quantity']
    filterset_class = CourseFilter