from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import Http404
from users.forms import AddUserForm


@login_required(login_url='stores:login')
def index(request):
    users = User.objects.all()

    return render(
        request,
        'users/index.html',
        {
            'users': users
        }
    )


@login_required(login_url='stores:login')
def add_user(request):
    form_action = reverse('users:add_user')

    if request.method == 'POST':
        form_user = AddUserForm(request.POST)

        context = {
            'form_user': form_user,
            'form_action': form_action
        }

        if form_user.is_valid():
            user = form_user.save(commit=False)
            password = form_user.cleaned_data.get('password')
            user.set_password(password)
            user.save()
            return redirect('users:index')

        return render(
            request,
            'users/add_user.html',
            context
        )

    context = {
        'form_user': AddUserForm(),
        'form_action': form_action,
    }

    return render(
        request,
        'users/add_user.html',
        context
    )


@login_required(login_url='stores:login')
def update_user(request, _id):
    user = get_object_or_404(User, pk=_id)

    if user.is_superuser:
        raise Http404

    form = AddUserForm(instance=user)

    if request.method == 'POST':
        form = AddUserForm(
            data=request.POST, instance=user)

        if form.is_valid():
            form.save()
            return redirect('users:update_user', _id=user.pk)

        return render(
            request,
            'users/add_user.html',
            {
                'form_user': form,
            }
        )

    return render(
        request,
        'users/add_user.html',
        {
            'form_user': form,
        }
    )


@login_required(login_url='stores:login')
def remove_user(request, _id):
    user = get_object_or_404(User, pk=_id)

    if user.is_superuser:
        raise Http404

    confirmation = request.POST.get('confirmation', 'no')

    if confirmation == 'yes':
        user.delete()
        return redirect('users:index')

    return render(
        request,
        'users/remove_user.html',
        {
            'user': user,
            'confirmation': confirmation,
        }
    )
