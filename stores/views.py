from django.shortcuts import render
from stores.models import Employee, Store


def index(request):
    employees = Employee.objects.all()

    context = {
        'employees': employees
    }

    return render(
        request,
        'stores/index.html',
        context
    )
