from django.contrib import admin
from django.http.request import HttpRequest
from stores.models import Store, Employee


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'function', 'store',)
    list_display_links = ('id', 'name', 'function', 'store',)
    search_fields = ('id', 'name', 'function', 'store',)


class EmployeeInline(admin.TabularInline):
    model = Employee
    extra = 1


@admin.register(Store)
class StoreAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'owner',)
    list_display_links = ('id', 'name', 'owner',)
    search_fields = ('id', 'name', 'owner',)
    inlines = (EmployeeInline,)

    def has_add_permission(self, request: HttpRequest) -> bool:
        return not Store.objects.exists()
