from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=50, null=True)
    author_name = models.CharField(max_length=50, null=True)
    author_surname = models.CharField(max_length=50, null=True)

    publication_year = models.IntegerField(null=True)
    page_count = models.IntegerField(null=True)

    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.title} - {self.author_name}"


class Reader(models.Model):
    name = models.CharField(max_length=30, null=True)
    surname = models.CharField(max_length=30, null=True)
    age = models.IntegerField(null=True)
    address = models.CharField(max_length=30, null=True)

    def __str__(self):
        return f"{self.name} - {self.surname} - {self.age}"


class BookRent(models.Model):
    book = models.ManyToManyField(Book)
    rent_date = models.DateField(null=True)
    reader = models.ManyToManyField(Reader)
    return_date = models.DateField(null=True)



    def __str__(self):
        book = self.book.first()
        book_title = book.title if book is not None else "unknown book"
        reader = self.reader.first()
        reader_surname = reader.surname if reader is not None else "unknown reader"
        return f"{book_title} was rent to {reader_surname}: {self.rent_date} - {self.return_date}"

