from django.db import models


class Store(models.Model):
    class Meta:
        verbose_name = 'Store'
        verbose_name_plural = 'Stores'

    name = models.CharField(max_length=50)
    description = models.CharField(max_length=255, blank=True)
    location = models.CharField(max_length=255, blank=True)
    owner = models.CharField(max_length=155, blank=True)

    def __str__(self) -> str:
        return self.name


class Employee(models.Model):
    class Meta:
        verbose_name = 'Employee'
        verbose_name_plural = 'Employees'

    name = models.CharField(max_length=155)
    birthday = models.DateField()
    function = models.CharField(max_length=50)
    store = models.ForeignKey(
        'Store', on_delete=models.SET_NULL, blank=True,
        null=True, default=None,
    )

    def __str__(self) -> str:
        return self.name
