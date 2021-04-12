from django.shortcuts import render, redirect
from .models import CustomUser
from .forms import CustomUserForm


def index(request):
    return render(request, 'index.html')


def get_all_users(request):
    users = CustomUser.objects.order_by('id')
    context = {'users': users}
    return render(request, 'user/all_user.html', context)


def get_by_id(request, id):
    full = CustomUser.get_by_id(id)
    return render(request, 'user/user.html', {'full': full})


def user_delete(request, delete_id):
    CustomUser.delete_by_id(delete_id)
    return redirect('get_all_users')


def user_form(request, id=0):
    if request.method == 'GET':
        if id == 0:
            form = CustomUserForm()
        else:
            user = CustomUser.get_by_id(id)
            form = CustomUserForm(instance=user)
        return render(request, 'user/user_form.html', {'form': form})
    else:
        if id == 0:
            form = CustomUserForm(request.POST)
        else:
            user = CustomUser.get_by_id(id)
            form = CustomUserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
        return redirect('get_all_users')
