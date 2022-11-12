from rest_framework import serializers
from .models import Location

# class LocatoinSerializer(serializers.ModelSerializer):

#     class Meta:
#         model = Location
#         fields = ('lat', 'lon')

#     lat = serializers.FloatField()
#     lon = serializers.FloatField()

#     def create(self, valid_data):
#         return Location.objects.create(**valid_data)