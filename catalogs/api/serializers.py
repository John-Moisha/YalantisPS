from rest_framework import serializers
from catalogs.models import Course


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
