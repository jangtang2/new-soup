from django.shortcuts import render
from . import models


def all_places(request):
    all_places = models.Place.objects.all()
    return render(request, "places/home.html", context={"places": all_places})


# Create your views here.
