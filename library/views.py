from django.shortcuts import render
from library.models import Book,  Reader, BookRent


# Create your views here.
def show_start_page(request):
    return render(request, "index.html")


def show_showbooks_page(request):
    context = {"books": Book.objects.all()}

    return render(request, "showBooks.html", context=context)


def show_addbook_page(request):
    if request.method == "POST":

        book_title = request.POST.get("book_title")
        author_name = request.POST.get("book_author_name")
        author_surname = request.POST.get("book_author_surname")
        genre = request.POST.get("book_genre")
        publication_year = request.POST.get("publication_year")
        page_count = request.POST.get("page_count")
        description = request.POST.get("description")

        newBook = Book(title=book_title,
                       author_name=author_name,
                       author_surname=author_surname,
                       publication_year=publication_year,
                       page_count=page_count,
                       description=description)
        newBook.save()



    return render(request, "addbook.html")


def show_addreader_page(request):
    if request.method == "POST":
        name = request.POST.get("reader_name")
        surname = request.POST.get("reader_surname")
        age = request.POST.get("reader_age")
        address = request.POST.get("reader_address")

        NewReader = Reader(name=name,
                           surname=surname,
                           age=age,
                           address=address)
        NewReader.save()

    return render(request, "addReader.html")


def show_add_rent_page(request):
    books = Book.objects.all()
    readers = Reader.objects.all()
    context = {'books': books, 'readers': readers}
    if request.method == "POST":
        book_id = request.POST.get("book_id")
        reader_id = request.POST.get("reader_id")
        rent_date = request.POST.get("rent_date")
        return_date = request.POST.get("return_date")

        book = Book.objects.get(id=book_id)
        reader = Reader.objects.get(id=reader_id)

        book_rent = BookRent.objects.create(rent_date=rent_date, return_date=return_date)
        book_rent.book.set([book])
        book_rent.reader.set([reader])

    return render(request, "addRent.html", context=context)

def show_readers(request):
    context = {'readers':Reader.objects.all()}

    return render(request, 'showReaders.html', context=context)

def show_rents(request):
    context = {'rents':BookRent.objects.all()}

    return render(request, 'showRent.html', context=context)

def remove_book(request):
    context = {'books': Book.objects.all()}
    if request.method == 'POST':
        book = request.POST.get('book_id')
        Book.objects.get(pk = book).delete()

    return render(request, 'removeBook.html', context)

def remove_reader(request):
    context = {'readers': Reader.objects.all()}
    if request.method == 'POST':
        reader = request.POST.get('reader_id')
        Reader.objects.get(pk=reader).delete()

    return render(request, 'removeReader.html', context=context)

def remove_rent(request):
    context = {'books': Book.objects.all(), 'readers': Reader.objects.all()}
    if request.method == 'POST':
        book_id = request.POST.get('book_id')
        reader_id = reader = request.POST.get('reader_id')

        rent = BookRent.objects.filter(
            book__id=book_id,
            reader__surname=reader_id
        )


        rent.delete()

    return render(request, 'removeRent.html', context=context)
