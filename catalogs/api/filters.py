from django_filters import rest_framework as filters

from catalogs.models import Course, Category


class CourseFilter(filters.FilterSet):
    class Meta:
        model = Course
        fields = {
            'title_course',
            'date_start',
            'date_end',
            'quantity'
        }

class CategoryFilter(filters.FilterSet):
    class Meta:
        model = Category
        fields = {
            'title_category'
        }