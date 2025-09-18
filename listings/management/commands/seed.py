from django.core.management.base import BaseCommand
from listings.models import Listing


class Command(BaseCommand):
    help = "Seed the database with sample listings"

    def handle(self, *args, **kwargs):
        sample_listings = [
            {"title": "Beach Resort", "description": "A relaxing beachside resort.",
             "location": "Mombasa", "price": 120.00},
            {"title": "Mountain Cabin", "description": "Cozy cabin with mountain views.",
             "location": "Mt. Kenya", "price": 85.50},
            {"title": "City Apartment", "description": "Modern apartment in city center.",
             "location": "Nairobi", "price": 100.00},
        ]

        for data in sample_listings:
            listing, created = Listing.objects.get_or_create(
                title=data["title"],
                defaults={
                    "description": data["description"],
                    "location": data["location"],
                    "price": data["price"]
                }
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f"Created listing: {listing.title}"))
            else:
                self.stdout.write(self.style.WARNING(f"Listing already exists: {listing.title}"))
