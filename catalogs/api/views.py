from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from catalogs.api.filters import CourseFilter
from catalogs.api.serializers import CourseSerializer
from catalogs.models import Course


class CourseModelViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    ordering_fields = ['title_course', 'date_start', 'date_end', 'quantity']
    filterset_class = CourseFilter
    search_fields = ['title_course']
