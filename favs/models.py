from django.db import models
from core import models as core_models


class Fav(core_models.TimeStampedModel):

    """Fav Model Def"""

    name = models.CharField(max_length=80)
    user = models.ForeignKey("users.User", on_delete=models.CASCADE)
    places = models.ManyToManyField("places.Place", blank=True)

    def __str__(self):
        return self.name
