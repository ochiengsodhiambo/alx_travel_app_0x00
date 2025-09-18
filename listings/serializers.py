from rest_framework import serializers
from .models import Listing, Booking


class ListingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Listing
        fields = ["id", "title", "description", "location", "price_per_night", "created_at"]


class BookingSerializer(serializers.ModelSerializer):
    listing = ListingSerializer(read_only=True)

    class Meta:
        model = Booking
        fields = ["id", "listing", "user", "start_date", "end_date", "guests", "created_at"]
        read_only_fields = ["user", "created_at"]
