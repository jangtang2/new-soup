from django.core.management.base import BaseCommand
from places.models import Facility


class Command(BaseCommand):
    help = "this command creates facilities"

    def handle(self, *args, **options):
        facilities = [
            "일반 야영장",
            "자동차 야영장",
            "카라반",
            "글램핑 시설",
            "잔디",
            "데크",
            "객실 내부 침대 구비",
            "객실 내부 TV 구비",
            "객실 내부 에어컨 구비",
            "객실 내부 냉장고 구비",
            "객실 내부 유무선 인터넷 구비",
            "객실 내부 난방기구 구비",
            "객실 내부 취사도구 구비",
            "객실 내부 화장실",
        ]

        for f in facilities:
            Facility.objects.create(name=f)
        self.stdout.write(self.style.SUCCESS("Facilities created"))
