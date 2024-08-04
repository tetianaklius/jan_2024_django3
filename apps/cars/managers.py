from django.db import models


class CarQuerySet(models.QuerySet):
    def less_than_year(self, year):
        return self.filter(year__lt=year)

    def only_smth(self):
        return self.filter(brand="smth")


class CarManager(models.Manager):
    def get_queryset(self):
        return CarQuerySet(self.model)

    def less_than_year(self, year):
        return self.get_queryset().less_than_year(year)

    def only_smth(self):
        return self.get_queryset().only_smth()