from django.views.generic import ListView
from books.models import BookList

class HomeListView(ListView):
    model= BookList
    context_object_name= 'all_books'
    template_name= 'main/home.html'
