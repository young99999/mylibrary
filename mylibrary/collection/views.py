from django.shortcuts import render

# Create your views here.
import json
from django.http import HttpResponse, Http404

from collection.models import Book, Author

def books_list(request):
	#books = [str(b) for b in Book.objects.all()]
	#return HttpResponse(json.dumps(books))
	books = Book.objects.order_by('-rating')
	return render(request, 'collection/books_list.html', {'books': books})
	

def book_details(request, book_id):
    try:
        book = Book.objects.get(pk=book_id)
    except Book.DoesNotExist:
        raise Http404("Book does not exist")
    '''
    data = {
        'title': book.title,
        'author': book.author.full_name,
        'pub_year': book.pub_year,
        'isbn': book.isbn,
        'rating': book.rating,
        'notes': book.notes,
        'id': book.id
    }
    return HttpResponse(json.dumps(data))
    '''
    return render(request, 'collection/book_details.html', {'book': book})

def authors_list(request):
    authors = [str(a) for a in Author.objects.all()]
    #return HttpResponse(json.dumps(authors))
    return render(request, 'collection/authors_list.html', {'authors': authors})
 
 
def author_details(request, author_id):
    try:
        author = Author.objects.get(pk=author_id)
    except Author.DoesNotExist:
        raise Http404("Author does not exist")
    #return HttpResponse(json.dumps(str(author)))
    return render(request, 'collection/author_details.html', {'author': author, 'books': books})