from django.db import models
from datetime import date
# Create your models here.


class Course(models.Model):
    title_course = models.CharField(max_length=128)
    date_start = models.DateField(null=True, blank=True)
    date_end = models.DateField(null=True, blank=True)
    quantity = models.SmallIntegerField()

    def clean(self):
        if self.date_start < date.today():
            raise ValueError("you can't create course in the past")
        elif self.date_start > self.date_end:
            raise ValueError(f'{self.date_end} cannot be before {self.date_start}')

    def save(self, **kwargs):
        self.clean()
        return super().save(**kwargs)

class Catalog(models.Model):
    title_category = models.CharField(max_length=128)
    course = models.ManyToManyField(Course)
