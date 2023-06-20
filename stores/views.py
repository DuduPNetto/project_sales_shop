from django.shortcuts import render
from stores.models import Employee, Store


def index(request):
    employees = Employee.objects.all()
    store = Store.objects.get()

    context = {
        'employees': employees,
        'store_title': store.name
    }

    return render(
        request,
        'stores/index.html',
        context
    )
