import random
from django.core.management.base import BaseCommand
from django_seed import Seed
from reviews import models as review_models
from users import models as user_models
from places import models as place_models


class Command(BaseCommand):
    help = "this command creates reviews"

    def add_arguments(self, parser):
        parser.add_argument(
            "--number",
            default=2,
            type=int,
            help="how many reviews do you want to create?",
        )

    def handle(self, *args, **options):
        number = options.get("number")
        seeder = Seed.seeder()
        users = user_models.User.objects.all()
        places = place_models.Place.objects.all()
        seeder.add_entity(
            review_models.Review,
            number,
            {
                "location": lambda x: random.randint(0, 5),
                "cleanliness": lambda x: random.randint(0, 5),
                "environmet": lambda x: random.randint(0, 5),
                "place": lambda x: random.choice(places),
                "user": lambda x: random.choice(users),
            },
        )
        seeder.execute()
        self.stdout.write(self.style.SUCCESS("reviews are created"))
