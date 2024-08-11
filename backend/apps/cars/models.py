from datetime import datetime

from django.core import validators as v
from django.db import models

from core.models import BaseModel
from core.services.file_service import FileService

from apps.auto_parks.models import AutoParkModel
from apps.cars.choices.body_type_choices import BodyTypeChoices
from apps.cars.managers import CarManager


class CarModel(BaseModel):
    class Meta:
        db_table = 'cars'
        ordering = ('id',)

    brand = models.CharField(max_length=20, validators=[v.MinLengthValidator(2)])
    price = models.IntegerField(validators=[v.MinValueValidator(0), v.MaxValueValidator(1000000)])
    year = models.IntegerField(validators=[v.MinValueValidator(1990), v.MaxValueValidator(datetime.now().year)])
    body_type = models.CharField(max_length=9, choices=BodyTypeChoices.choices)
    auto_park = models.ForeignKey(AutoParkModel, on_delete=models.CASCADE, related_name='cars')
    photo = models.ImageField(upload_to=FileService.upload_car_photo, blank=True)

    objects = CarManager()
