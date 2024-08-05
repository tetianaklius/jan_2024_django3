from rest_framework import serializers

from apps.cars.models import CarModel


class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarModel
        fields = ('id', 'brand', 'price', 'body_type', 'year', 'photo', 'created_at', 'updated_at')


class CarPhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarModel
        fields = ('photo',)
        extra_kwargs = {'photo': {'required': True}}

