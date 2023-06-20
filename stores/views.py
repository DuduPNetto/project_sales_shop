from django.shortcuts import render
from django.urls import reverse
from stores.models import Employee, Store
from stores.forms import AddEmployeeForm


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


def add_employee(request):
    form_action = reverse('stores:add_employee')

    if request.method == 'POST':
        form_employee = AddEmployeeForm(request.POST)

        context = {
            'form_employee': form_employee,
            'form_action': form_action
        }

        return render(
            request,
            'stores/add_employee.html',
            context
        )

    context = {
        'form': AddEmployeeForm(),
        'form_action': form_action,
    }

    return render(
        request,
        'stores/add_employee.html',
        context
    )


def remove_employee(request):

    context = {

    }

    return render(
        request,
        'stores/remove_employee.html',
        context
    )
