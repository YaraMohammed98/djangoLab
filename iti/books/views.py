from pydoc import describe
from django.shortcuts import render , get_object_or_404,redirect
import json
from multiprocessing import context
from django.http import HttpResponse

from .forms import BookForm
from .models import Book
from .models import Author




# with open('C:/Users/yaraa/books.txt','r') as file:
#        books = json.load(file)


# Create your views here.
def index(request):

    context = {
        "books": Book.objects.all()
    }
    return render(request,"books/index.html", context=context)

def book(request,book_id):
    book=get_object_or_404(Book,id=book_id)
    context= {
        "book":book

    }
    return render(request,"books/book.html", context=context)

def author(request,author_id):
    books=Book.objects.filter(author=author_id).all()
    context= {
        "author":books[0].author,
        "books":books
    }
    return render(request,"books/author.html", context=context)
    
def new(request):
    if request.method=="POST":
        form=BookForm(request.POST)
        if form.is_valid():
            book=form.save()
            return redirect("book_info",book_id=book.id)
    else:
            form=BookForm()    
    return render(request, "books/book_create.html", context={"form":form})
 

def edit(request,book_id):
    book=get_object_or_404(Book,id=book_id)
    if request.method=="POST":
        form=BookForm(request.POST,instance=book)
        if form.is_valid():
            book=form.save()
            return redirect("book_info",book_id=book.id)
    else:
            form=BookForm(instance=book)    
    return render(request, "books/book_create.html", context={"form":form})
 
def delete(request,book_id):
    book=get_object_or_404(Book,id=book_id)
    if request.method=="POST":
        book.delete()
        return redirect("home")
    context={'item':book}
    return render(request, "books/delete.html", context)
  