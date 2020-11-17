from django.views.generic import ListView
from . import models


class HomeView(ListView):
    model = models.Place
    paginate_by = 10
    paginate_orphans = 5
    ordering = "created"


# Create your views here.
