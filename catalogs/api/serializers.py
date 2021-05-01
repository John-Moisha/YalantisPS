from rest_framework import serializers
from catalogs.models import Course, Catalog


class CourseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Course
        fields = (
            'id',
            'title_course',
            'date_start',
            'date_end',
            'quantity',
        )


class CatalogSerializer(serializers.ModelSerializer):

    class Meta:
        model = Catalog
        fields = (
            'id',
            'title_category',
            'course',
        )
