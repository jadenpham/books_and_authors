from django.shortcuts import render, redirect, HttpResponse
from . import models

def index(request):
    book_info = models.Book.objects.all()
    context = {
        "book_info": book_info
    }
    return render(request, "books_authors_app/index.html", context)

def add_book(request):
    if request.method=="POST":
        models.Book.objects.create(title = request.POST['book_title'], description = request.POST['book_descrip'])
    return redirect('/')

def book_info(request, book_id):
    books = models.Book.objects.get(id=book_id)
    context={
        "book_title": books.title,
        "book_id": books.id,
        "book_descp": books.description,
        "authors": models.Book.objects.get(id=book_id).authors.all(),
        "all_authors": models.Author.objects.all()
    }
    print(context)
    return render(request, 'books_authors_app/views.html', context)

def add_author(request,book_id):
    if request.method == "POST":
        models.Book.objects.get(id=book_id).authors.add(models.Author.objects.get(id=request.POST["author_id"]))
        return redirect('/book_info/'+book_id)

def all_authors(request):
    context={
        "all_authors": models.Author.objects.all()
    }
    return render(request, "books_authors_app/authors.html", context)

def author_info(request, author_id):
    context ={
        "all_info": models.Author.objects.get(id=author_id),
        "related_books": models.Author.objects.get(id=author_id).books.all(),
        "all_books": models.Book.objects.all()
    }
    print(context)
    return render(request, "books_authors_app/author_info.html", context)

def new_author(request):
    if request.method == "POST":
        models.Author.objects.create(first_name = request.POST["first_name"], last_name=request.POST["last_name"], notes=request.POST["notes"])
    return redirect('/authors')

def book_to_author(request, author_id):
    if request.method == "POST":
        author=models.Author.objects.get(id=author_id)
        models.Book.objects.get(id=request.POST["new_book"]).authors.add(author)
    return redirect('/authors/'+author_id)