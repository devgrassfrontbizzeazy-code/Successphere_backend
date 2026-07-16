
from django.core.management.base import BaseCommand

from products.models import Category


class Command(BaseCommand):
    help = "Seed the Category table with initial data"

    def handle(self, *args, **options):
        categories = [
            (1, "Spices"),
            (2, "Vegetables"),
            (3, "Organic Food Products"),
            (4, "Handicrafts"),
            (5, "God Statues"),
            (6, "Copper Vessels"),
            (7, "Garments"),
            (8, "Minerals"),
            (9, "Construction Materials"),
        ]

        for cat_id, name in categories:
            obj, created = Category.objects.update_or_create(
                id=cat_id, defaults={"name": name}
            )
            status = "Created" if created else "Exists"
            self.stdout.write(f"  {status}: [{cat_id}] {name}")

        self.stdout.write(self.style.SUCCESS("\nAll 9 categories seeded!"))
