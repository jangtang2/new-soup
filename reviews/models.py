from django.db import models
from core import models as core_models


class Review(core_models.TimeStampedModel):

    """Review Model Def"""

    review = models.TextField()
    cleanliness = models.IntegerField()
    location = models.IntegerField()
    environmet = models.IntegerField()
    user = models.ForeignKey("users.User", on_delete=models.CASCADE)
    place = models.ForeignKey("places.Place", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.review} - {self.place}"

    def rating_average(self):
        avg = (self.cleanliness + self.location + self.environmet) / 3
        return round(avg, 1)
