from django.shortcuts import render, redirect
from .models import Book
from .forms import BookForm


def get_all_books(request):
    books = Book.objects.all()
    context = {'books': books}
    return render(request, 'book/all_books.html', context)


def get_book(request, id):
    full = Book.get_by_id(id)
    return render(request, 'book/book.html', {'full': full})


def book_form(request, id=0):
    if request.method == 'GET':
        if id == 0:
            form = BookForm()
        else:
            book = Book.get_by_id(id)
            form = BookForm(instance=book)
        return render(request, 'book/book_form.html', {'form': form})
    else:
        if id == 0:
            form = BookForm(request.POST)
        else:
            book = Book.get_by_id(id)
            form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
        return redirect('get_all_books')


def delete_book(request, id):
    Book.delete_by_id(id)
    return redirect('get_all_books')
