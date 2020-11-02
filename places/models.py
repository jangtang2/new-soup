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

    class Meta:
        verbose_name_plural = "Amenities"


class Facility(AbstractItem):

    """Facility Model Def"""

    class Meta:
        verbose_name_plural = "Facilities"


class ETC(AbstractItem):

    """ETC Model Def"""

    class Meta:
        verbose_name = "ETC"


class Photo(core_models.TimeStampedModel):

    """Photo Model Def"""

    file = models.ImageField(upload_to="place_photos")
    place = models.ForeignKey("place", related_name="photos", on_delete=models.CASCADE)


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
    amenities = models.ManyToManyField("Amenity", blank=True)
    facilities = models.ManyToManyField("Facility", blank=True)
    etcs = models.ManyToManyField("ETC", blank=True)

    def __str__(self):
        return self.name

    def total_rating(self):
        all_reviews = self.reviews.all()
        all_ratings = 0
        for review in all_reviews:
            all_ratings += review.rating_average()
        return all_ratings / len(all_reviews)
