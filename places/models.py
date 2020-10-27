from django.db import models
from django_countries.fields import CountryField
from core import models as core_models

# Create your models here.


class AbstractItem(core_models.TimeStampedModel):

    """Abstract Item"""

    name = models.CharField(max_length=80)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name


class Amenity(AbstractItem):

    """Amenity Model Def"""

    pass


class Facility(AbstractItem):

    """Facility Model Def"""

    pass


class ETC(AbstractItem):

    """ETC Model Def"""

    pass


class Place(core_models.TimeStampedModel):

    """ Place Model Def"""

    name = models.CharField(max_length=140)
    description = models.TextField()
    country = CountryField()
    city = models.CharField(max_length=80)
    address = models.CharField(max_length=140)
    toilets = models.IntegerField()
    showerbooths = models.IntegerField()
    booklinks = models.URLField()
    amenities = models.ManyToManyField(Amenity)
    facilities = models.ManyToManyField(Facility)
    etcs = models.ManyToManyField(ETC)

    def __str__(self):
        return self.name