from rest_framework import serializers
from catalogs.models import Course, Category


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


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = (
            'id'
            'title_category',
        )
