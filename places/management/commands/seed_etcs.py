from django.core.management.base import BaseCommand
from places.models import ETC


class Command(BaseCommand):
    help = "this command creates etcs"

    def handle(self, *args, **options):
        etcs = [
            "텐트 대여",
            "릴선 대여",
            "화로대 대여",
            "난방기구 대여",
            "식기 대여",
            "침낭 대여",
            "애완동물 출입 가능",
            "개별 화로대",
            "장작 무료",
        ]
        for e in etcs:
            ETC.objects.create(name=e)
        self.stdout.write(self.style.SUCCESS("ETCs are created"))
