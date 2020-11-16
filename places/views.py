from math import ceil
from django.shortcuts import render
from django.core.paginator import Paginator
from . import models


def all_places(request):
    page = request.GET.get("page", 1)
    place_list = models.Place.objects.all()
    paginator = Paginator(place_list, 10, orphans=5)
    places = paginator.get_page(int(page))

    return render(
        request,
        "places/home.html",
        {"places": places},
    )


# Create your views here.
