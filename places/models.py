from django.db import models
from django_countries.fields import CountryField
from core import models as core_models

# Create your models here.


class Place(core_models.TimeStampedModel):

    """ Place Model Def"""

    name = models.CharField(max_length=140)
    description = models.TextField()
    country = CountryField()
    city = models.CharField(max_length=80)
    address = models.CharField(max_length=140)
    toilets = models.IntegerField()
    showerbooths = models.IntegerField()
    operdays = models.DateField()
    booklinks = models.URLField()