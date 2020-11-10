import random
from django.core.management.base import BaseCommand
from django.contrib.admin.utils import flatten
from django_seed import Seed
from places import models as place_models


class Command(BaseCommand):
    help = "this command creates many users"

    def add_arguments(self, parser):
        parser.add_argument(
            "--number",
            default=1,
            type=int,
            help="how many places do you want to create?",
        )

    def handle(self, *args, **options):
        number = options.get("number")
        seeder = Seed.seeder()
        seeder.add_entity(
            place_models.Place,
            number,
            {
                "name": lambda x: seeder.faker.address(),
                "toilets": lambda x: random.randint(0, 10),
                "showerbooths": lambda x: random.randint(0, 10),
            },
        )
        created_photos = seeder.execute()
        created_clean = flatten(list(created_photos.values()))
        for pk in created_clean:
            place = place_models.Place.objects.get(pk=pk)
            for i in range(3, random.randint(5, 10)):
                place_models.Photo.objects.create(
                    place=place,
                    file=f"place_photo/{random.randint(1, 31)}.jpg",
                )
        self.stdout.write(self.style.SUCCESS("places are created"))
