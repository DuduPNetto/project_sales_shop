from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.http import Http404
from django.contrib import auth
from stores import models
from stores.forms import AddEmployeeForm, AddProductForm
from django.contrib.auth.forms import AuthenticationForm


def index(request):
    products = models.StoreProduct.objects.all()

    return render(
        request,
        'stores/index.html',
        {
            'products': products
        }
    )


@login_required(login_url="stores:login")
def add_product(request):
    form_action = reverse('stores:add_product')

    if request.method == 'POST':
        form = AddProductForm(request.POST, request.FILES)

        context = {
            'form': form,
            'form_action': form_action
        }

        if form.is_valid():
            product = form.save(commit=False)
            product.save()
            return redirect('stores:index')

        return render(
            request,
            'stores/add_product.html',
            context
        )

    context = {
        'form': AddProductForm(),
        'form_action': form_action,
    }

    return render(
        request,
        'stores/add_product.html',
        context
    )


@login_required(login_url="stores:login")
def update_product(request, _id):
    product = get_object_or_404(models.StoreProduct, pk=_id)

    form = AddProductForm(instance=product)

    if request.method == 'POST':
        form = AddProductForm(
            data=request.POST, files=request.FILES, instance=product)

        if form.is_valid():
            form.save()
            return redirect('stores:update_product', _id=product.pk)

        return render(
            request,
            'stores/add_product.html',
            {
                'form': form,
            }
        )

    return render(
        request,
        'stores/add_product.html',
        {
            'form': form,
        }
    )


@login_required(login_url="stores:login")
def remove_product(request, _id):
    product = get_object_or_404(models.StoreProduct, pk=_id)

    confirmation = request.POST.get('confirmation', 'no')

    if confirmation == 'yes':
        product.delete()
        return redirect('stores:index')

    return render(
        request,
        'stores/remove_product.html',
        {
            'product': product,
            'confirmation': confirmation,
        }
    )


@login_required(login_url="stores:login")
def all_employees(request):
    employees = models.Employee.objects.all()

    context = {
        'employees': employees
    }

    return render(
        request,
        'stores/all_employees.html',
        context
    )


@login_required(login_url="stores:login")
def add_employee(request):
    form_action = reverse('stores:add_employee')

    if request.method == 'POST':
        form_employee = AddEmployeeForm(request.POST)

        context = {
            'form_employee': form_employee,
            'form_action': form_action
        }

        if form_employee.is_valid():
            employee = form_employee.save(commit=False)
            employee.save()
            return redirect('stores:all_employees')

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


@login_required(login_url="stores:login")
def update_employee(request, _id):
    employee = get_object_or_404(models.Employee, pk=_id)

    form = AddEmployeeForm(instance=employee)

    if request.method == 'POST':
        form = AddEmployeeForm(
            data=request.POST, files=request.FILES, instance=employee)

        if form.is_valid():
            form.save()
            return redirect('stores:update_employee', _id=employee.pk)

        return render(
            request,
            'stores/add_employee.html',
            {
                'form': form,
            }
        )

    return render(
        request,
        'stores/add_employee.html',
        {
            'form': form,
        }
    )


@login_required(login_url="stores:login")
def employee_detail(request, _id):
    employee = get_object_or_404(models.Employee, pk=_id)

    return render(
        request,
        'stores/employee_detail.html',
        {
            'employee': employee,
        }
    )


@login_required(login_url="stores:login")
def remove_employee(request, _id):

    employee = get_object_or_404(models.Employee, pk=_id)

    if employee.function == 'Owner':
        raise Http404()

    confirmation = request.POST.get('confirmation', 'no')

    if confirmation == 'yes':
        employee.delete()
        return redirect('stores:all_employees')

    return render(
        request,
        'stores/remove_employee.html',
        {
            'employee': employee,
            'confirmation': confirmation,
        }
    )


def login(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        if not username or not password:
            return redirect('stores:login')

        user = auth.authenticate(
            request, username=username, password=password
        )

        if user:
            auth.login(request, user=user)
            return redirect('stores:index')
        else:
            return redirect('stores:login')

    return render(
        request,
        'stores/login.html'
    )


@login_required(login_url="stores:login")
def logout(request):

    auth.logout(request)
    return redirect('stores:login')
