from django.views.generic import ListView
from django.shortcuts import render
from . import models


class HomeView(ListView):
    model = models.Place
    paginate_by = 10
    paginate_orphans = 5
    ordering = "created"
    context_object_name = "places"


def place_detail(request, pk):
    print(pk)
    return render(request, "places/detail.html")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        now = timezone.now()
        context["now"] = now
        return context


# Create your views here.
