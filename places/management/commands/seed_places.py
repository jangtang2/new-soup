from django.core.management.base import BaseCommand
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
        )
        seeder.execute()
        self.stdout.write(self.style.SUCCESS("places are created"))
