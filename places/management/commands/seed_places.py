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

        amenities = place_models.Amenity.objects.all()
        facilities = place_models.Facility.objects.all()
        etcs = place_models.ETC.objects.all()
        for pk in created_clean:
            placet = place_models.Place.objects.get(pk=pk)
            for i in range(3, random.randint(5, 15)):
                place_models.Photo.objects.create(
                    place=placet,
                    file=f"place_photo/{random.randint(1, 31)}.jpg",
                )
            for a in amenities:
                magic_number = random.randint(0, 15)
                if magic_number % 2 == 0:
                    placet.amenities.add(a)
            for f in facilities:
                magic_number = random.randint(0, 15)
                if magic_number % 2 == 0:
                    placet.facilities.add(f)
            for e in etcs:
                magic_number = random.randint(0, 15)
                if magic_number % 2 == 0:
                    placet.etcs.add(e)

        self.stdout.write(self.style.SUCCESS("places are created"))
