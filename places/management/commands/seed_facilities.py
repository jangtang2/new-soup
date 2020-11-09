from django.core.management.base import BaseCommand
from places.models import Amenity


class Command(BaseCommand):
    help = "this command creates facilities"

    def handle(self, *args, **options):
        amenities = [
            "전기",
            "와이파이",
            "장작판매",
            "온수",
            "산책로",
            "물놀이장",
            "운동시설",
            "마트, 편의점",
            "놀이터" "운동장",
            "트램폴린",
        ]
        for a in amenities:
            Amenity.objects.create(name=a)
        self.stdout.write(self.style.SUCCESS("Amenities created"))
