from django_filters import rest_framework as filters

from catalogs.models import Course


class CourseFilter(filters.FilterSet):
    class Meta:
        model = Course
        fields = {
            'date_start': ['gte'],
            'date_end': ['lte'],
        }
