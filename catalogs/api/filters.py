from django_filters import rest_framework as filters

from catalogs.models import Course, Catalog


class CourseFilter(filters.FilterSet):
    class Meta:
        model = Course
        fields = {
            'title_course',
            'date_start',
            'date_end',
            'quantity'
        }


class CatalogFilter(filters.FilterSet):
    class Meta:
        model = Catalog
        fields = {
            'title_category'
        }
