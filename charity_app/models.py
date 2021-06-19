from django.db import models

# Create your models here.

TYPE = (
    (1, "fundacja"),
    (2, "organizacja pozarządowa"),
    (3, "Zbiórka lokalna"),
    (4, "domyślnie fundacja")

)


class Category(models.Model):
    name = models.CharField(max_length=64)


class Institution(models.Model):
    name = models.CharField(max_length=64)
    description = models.CharField(max_length=64)
    type = models.IntegerField(choices=TYPE)
    categories = models.ManyToManyField('Category')
