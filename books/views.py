from django.http import Http404
from django.shortcuts import render
from .models import Book

sort_count = {'image_link': 0, 'author': 0, 'country': 0, 'language': 0, 'pages': 0, 'title': 0, 'year': 0}


def index(request):
	global sort_count
	all_books = Book.objects.all()
	sort_count = {'image_link': 0, 'author': 0, 'country': 0, 'language': 0, 'pages': 0, 'title': 0, 'year': 0}
	return render(request, 'books/home.html', {'all_books': all_books})


# http://127.0.0.1:8000/id | show you have this book in db or not
def detail(request, book_id):
	try:
		book = Book.objects.get(pk=book_id)
	except Book.DoesNotExist:
		raise Http404("Book does not exist")
	return render(request, 'books/detail.html', {'book': book})


def create_book(request, book):
	if request.method == 'POST':
		data = request.POST
		image_link, author, country, language, pages, title, year\
			= data['image_link'], data['author'], data['country'], data['language'], data['pages'], data['title'], data['year']
		try:
			Book.objects.get(image_link=image_link, author=author, country=country, language=language, pages=pages, title=title, year=year)
		except Book.DoesNotExist:
			Book.objects.create(image_link=image_link, author=author, country=country, language=language, pages=pages, title=title, year=year)
			return render(request, 'books/home.html', {'book': book})


def sort(request):
	global sort_count
	if request.method == 'POST':
		key = request.POST['sort_id'][2:]
		val = sort_count[key] + 1
		sort_count = {'image_link': 0, 'author': 0, 'country': 0, 'language': 0, 'pages': 0, 'title': 0, 'year': 0}
		sort_count[key] = val
		return render(request, 'books/home.html', {'all_book': Book.objects.order_by('-' * (1 - val % 2) + key)})


