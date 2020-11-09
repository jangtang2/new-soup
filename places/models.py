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

    CITY_CHOICES = (
        ("서울특별시", "서울특별시"),
        ("부산광역시", "부산광역시"),
        ("대구광역시", "대구광역시"),
        ("인천광역시", "인천광역시"),
        ("광주광역시", "광주광역시"),
        ("대전광역시", "대전광역시"),
        ("울산광역시", "울산광역시"),
        ("세종특별자치시", "세종특별자치시"),
        ("경기도", "경기도"),
        ("강원도", "강원도"),
        ("충청북도", "충청북도"),
        ("충청남도", "충청남도"),
        ("전라북도", "전라북도"),
        ("전라남도", "전라남도"),
        ("경상북도", "경상북도"),
        ("경상남도", "경상남도"),
        ("제주특별자치도", "제주특별자치도"),
    )

    name = models.CharField(max_length=140)
    description = models.TextField()
    country = CountryField()
    city = models.CharField(choices=CITY_CHOICES, max_length=80)
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
        if len(all_reviews) > 0:
            for review in all_reviews:
                all_ratings += review.rating_average()
            return all_ratings / len(all_reviews)
        return 0
