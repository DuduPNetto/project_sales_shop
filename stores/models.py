from django.db import models
from django.contrib.auth.models import User
from utils.resize_image import resize_image


class Store(models.Model):
    class Meta:
        verbose_name = 'Store'
        verbose_name_plural = 'Stores'

    name = models.CharField(max_length=50)
    description = models.CharField(max_length=255, blank=True)
    location = models.CharField(max_length=255, blank=True)
    owner = models.OneToOneField(
        User, on_delete=models.SET_NULL, null=True)

    def __str__(self) -> str:
        return self.name


class Employee(models.Model):
    class Meta:
        verbose_name = 'Employee'
        verbose_name_plural = 'Employees'

    name = models.CharField(max_length=155)
    age = models.PositiveIntegerField(default=18)
    function = models.CharField(max_length=50)
    email = models.EmailField(max_length=100, null=True)
    store = models.ForeignKey(
        'Store', on_delete=models.SET_NULL, blank=True,
        null=True, default=None,
    )

    def __str__(self) -> str:
        return self.name


class StoreProduct(models.Model):
    class Meta:
        verbose_name = 'StoreProduct'
        verbose_name_plural = 'StoreProducts'

    name = models.CharField(max_length=255)
    short_description = models.TextField(max_length=255, blank=True)
    long_description = models.TextField(blank=True)
    price = models.FloatField()
    stock = models.PositiveIntegerField()
    store = models.ForeignKey(
        Store, on_delete=models.CASCADE
    )
    image = models.ImageField(blank=True, upload_to='images/%Y/%m')

    def save(self, *args, **kwargs) -> None:
        super().save(*args, **kwargs)

        if self.image:
            resize_image(self.image)

    def __str__(self) -> str:
        return self.name
