from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404
from .models import Book


sort_count = {'author': 0, 'country': 0, 'image_link': 0, 'language': 0, 'link': 0, 'pages': 0, 'title': 0, 'year': 0}


def index(request):
	global sort_count
	all_books = Book.objects.all()
	sort_count = {'author': 0, 'country': 0, 'image_link': 0, 'language': 0, 'link': 0, 'pages': 0, 'title': 0, 'year': 0}
	return render(request, 'books/index.html', {'all_books': all_books})


def create_book(request):
	if request.method == 'POST':
		data = request.POST
		author, country, image_link, language, link, pages, title, year = \
			data['author'], data['country'], data['image_link'], data['language'], data['link'], data['pages'], data['title'],\
			data['year']
		try:
			Book.objects.get(author=author, country=country, image_link=image_link, language=language, link=link, pages=pages,
							title=title, year=year)
		except Book.DoesNotExist:
			Book.objects.create(author=author, country=country, image_link=image_link, language=language, link=link, pages=pages,
							title=title, year=year)
		return HttpResponse('')


def update_books(request):
	order_set = [(key, val) for key, val in sort_count.items() if val != 0]
	if order_set:
		key, val = order_set[0]
		order_set = Book.objects.order_by('-' * (1 - val % 2) + key)
	else:
		order_set = Book.objects.all()
	return render(request, 'books/index.html', {'all_books': order_set})


def sort(request):
	global sort_count
	if request.method == 'POST':
		key = request.POST['sort_id'][2:]
		val = sort_count[key] + 1
		sort_count = {'author': 0, 'country': 0, 'image_link': 0, 'language': 0, 'link': 0, 'pages': 0, 'title': 0, 'year': 0}
		sort_count[key] = val
		return render(request, 'books/index.html', {'all_book': Book.objects.order_by('-' * (1 - val % 2) + key)})


# http://127.0.0.1:8000/id | show you have this book in db or not
def detail(request, book_id):
	try:
		book = Book.objects.get(pk=book_id)
	except Book.DoesNotExist:
		raise Http404("Book does not exist")
	return render(request, 'books/detail.html', {'book': book})


