import random
from django.core.management.base import BaseCommand
from django.contrib.admin.utils import flatten
from django_seed import Seed
from favs import models as fav_models
from users import models as user_models
from places import models as place_models


class Command(BaseCommand):
    help = "this command creates favs"

    def add_arguments(self, parser):
        parser.add_argument(
            "--number",
            default=2,
            type=int,
            help="how many favs do you want to create?",
        )

    def handle(self, *args, **options):
        number = options.get("number")
        seeder = Seed.seeder()
        users = user_models.User.objects.all()
        places = place_models.Place.objects.all()
        seeder.add_entity(
            fav_models.Fav,
            number,
            {
                "user": lambda x: random.choice(users),
            },
        )
        created = seeder.execute()
        cleaned = flatten(list(created.values()))
        for pk in cleaned:
            fav_model = fav_models.Fav.objects.get(pk=pk)
            to_add = places[random.randint(0, 5) : random.randint(6, 15)]
            fav_model.places.add(*to_add)

        self.stdout.write(self.style.SUCCESS("favs are created"))
