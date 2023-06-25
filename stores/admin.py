from django.contrib import admin
from django.http.request import HttpRequest
from stores import models


@admin.register(models.Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'function', 'store',)
    list_display_links = ('id', 'store',)
    search_fields = ('id', 'name', 'function', 'store',)
    ordering = ('-id',)
    list_editable = ('name',)


class EmployeeInline(admin.TabularInline):
    model = models.Employee
    extra = 1


@admin.register(models.StoreProduct)
class StoreProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'short_description',
                    'price', 'stock', 'store')
    list_display_links = ('id',)
    search_fields = ('id', 'name', 'long_description', 'store',)
    ordering = ('-id',)
    list_editable = ('name', 'short_description', 'price')


class StoreProductInline(admin.TabularInline):
    model = models.StoreProduct
    extra = 1


@admin.register(models.Store)
class StoreAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'owner',)
    list_display_links = ('id', 'name', 'owner',)
    search_fields = ('id', 'name', 'owner',)
    inlines = (EmployeeInline, StoreProductInline)
