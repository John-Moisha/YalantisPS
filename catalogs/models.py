from django.db import models

# Create your models here.

class Course(models.Model):
    title_course = models.CharField(max_length=128)
    date_start = models.DateField(null=True)
    date_end = models.DateField(null=True)
    quantity = models.SmallIntegerField()

class Category(models.Model):
    title_category = models.CharField(max_length=128)
    course = models.ManyToManyField(Course)



