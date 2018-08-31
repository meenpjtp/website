from django.views.generic import TemplateView
from django.http import Http404
from django.shortcuts import render, redirect
from .models import Book
from books.forms import HomeForm


class HomeView(TemplateView):
	template_name = 'books/home.html'

	def get(self, request):
		form = HomeForm()
		return render(request, self.template_name, {'form': form})

	def post(self, request):
		form = HomeForm(request.POST)
		if form.is_valid():
			text = form.cleaned_data['post']
			form = HomeForm(request.POST)
			return redirect('books:books')

		args = {'form': form, 'text': text}
		return render(request, self.template_name, args)


def index(request):
	all_books = Book.objects.all()
	# context = {'all_books': all_books}
	return render(request, 'books/home.html', {'all_books': all_books})


def detail(request, book_id):
	try:
		book = Book.objects.get(pk=book_id)
	except Book.DoesNotExist:
		raise Http404("Book does not exist")
	return render(request, 'books/detail.html', {'book': book})

