from django.shortcuts import render, redirect
from book.forms import BookStoreForm
from book.models import BookStoreModel

# Create your views here.

def home(request):
    return render(request, 'home.html')

def store_book(request):
    if request.method == 'POST':
        book = BookStoreForm(request.POST, request.FILES)
        if book.is_valid():
            book.save()
            print(book.cleaned_data)
            return redirect('show_book')
    else:
        book = BookStoreForm()
    return render(request, 'store_book.html', {'form': book})

def show_book(request):
    book = BookStoreModel.objects.all()
    print(book);
    return render(request, 'show_book.html', {'data': book})

def edit_book(request, id):
    book = BookStoreModel.objects.get(pk = id)
    form = BookStoreForm(instance = book)
    if request.method == 'POST':
        update_book = BookStoreForm(request.POST, instance = book)
        if update_book.is_valid():
            update_book.save()
            print(update_book.cleaned_data)
            return redirect('show_book')
    return render(request, 'store_book.html', {'form': form})

def delete_book(request, id):
    book = BookStoreModel.objects.get(pk = id).delete()
    return redirect('show_book')
    