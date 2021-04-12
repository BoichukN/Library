from django.shortcuts import render, redirect
from .models import Order
from authors.models import Author
from book.models import Book
from .forms import OrderForm


def get_all_orders(request):
    orders = Order.objects.all()
    context = {'orders': orders}

    return render(request, 'order/all_order.html', context)


def get_order(request, id):
    full = Order.get_by_id(id)
    return render(request, 'order/order.html', {'full': full})


def order_form(request, id=0):
    if request.method == 'GET':
        if id == 0:
            form = OrderForm()
        else:
            order = Order.get_by_id(id)
            form = OrderForm(instance=order)
        return render(request, 'order/order_form.html', {'form': form})
    else:
        if id == 0:
            form = OrderForm(request.POST)
        else:
            order = Order.get_by_id(id)
            form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
        return redirect('get_all_orders')


def delete_order(request, id):
    Order.delete_by_id(id)
    return redirect('get_all_orders')
