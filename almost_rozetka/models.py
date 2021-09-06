from django.contrib.auth.models import AbstractUser
from django.db import models


class City(models.Model):
    city_name = models.CharField("city", max_length=250)

    class Meta:
        verbose_name = 'City'
        verbose_name_plural = 'Cities'

    def __str__(self):
        return f'{self.city_name}'


class Product(models.Model):
    product = models.CharField(max_length=250)
    price = models.FloatField(blank=True, null=True)

    def __str__(self):
        return f'{self.product} - {self.price}$'


class CustomUser(AbstractUser):
    product = models.ManyToManyField(Product, blank=True)
    city = models.ForeignKey(City, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return f'{self.username}'


class Company(models.Model):
    name = models.CharField("company", max_length=250)
    city = models.OneToOneField(City, on_delete=models.CASCADE, primary_key=True,)

    class Meta:
        verbose_name = 'Company'
        verbose_name_plural = 'Companies'

    def __str__(self):
        return f'{self.name} - {self.city}'
