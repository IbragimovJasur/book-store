from django.shortcuts import redirect, render
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from .models import BookList, Review
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q
from order.models import Order
from datetime import timedelta, datetime

class BookListView(ListView):
    model= BookList
    context_object_name= 'book_list'
    template_name= 'books/book_list.html'


class BookDetailView(LoginRequiredMixin, DetailView):
    model= BookList
    context_object_name= 'book'
    template_name= 'books/book_detail.html'
    pk_url_kwarg= 'pk'

#New book to sell
class BookCreateView(LoginRequiredMixin, CreateView):
    model= BookList
    template_name= 'books/create_book.html'
    fields= ['title', 'author', 'price', 'image',] 

    def form_valid(self, form):
        form.instance.posted_by_id = self.request.user.id
        return super(BookCreateView, self).form_valid(form)

#Update book info
class BookUpdateView(LoginRequiredMixin, UpdateView):
    model= BookList
    template_name= 'books/update_book.html'
    isinstance= BookList
    fields= ['title', 'author', 'price', 'image',]

#New comment
@login_required
def createreview(request, book_id):
    if request.method== "POST":
        book= BookList.objects.get(id= book_id)
        sentence= request.POST.get('sentence')
        print(sentence)
        if sentence != '':
            book.reviews.create(sentence=sentence, author_id= request.user.id)
            book.save()
            return redirect(f'/books/{book_id}')
        else:
            messages.info(request, 'Comment cannot be blank')
            return redirect(f'/books/{book_id}')

    return render(request, 'books/book_detail.html') 

#Search
class SearchResultListView(LoginRequiredMixin, ListView):
    model= BookList
    template_name= 'books/search_result.html'
    context_object_name= 'book_list'

    def get_queryset(self):
        query= self.request.GET.get('q')
        return BookList.objects.filter(Q(title__icontains= query) | Q(author__icontains= query))

#Delete comment
@login_required
def deletereview(request, book_id, review_id): #book_id for redirecting
    if request.method== 'POST':
        old= Review.objects.get(id= review_id)
        old.delete()
        return redirect(f'/books/{book_id}')

    return render(request, 'books/book_detail.html')
        
#New order
def neworder(request, book_id):
    if request.method== 'POST':
        ordered_by= request.user
        book= BookList.objects.get(id= book_id)
        card_number= request.POST['card_number']
        deliver_to= request.POST['deliver_to']
        
        if card_number != '' and deliver_to != '':
            date_of_order= request.POST['date_of_order']
            date_of_delivery= datetime.strptime(date_of_order, "%Y-%m-%dT%H:%M") + timedelta(days=5)
            model= Order(
                ordered_by= ordered_by, 
                book= book, 
                card_number= card_number, 
                date_of_order=date_of_order, 
                date_of_delivery= date_of_delivery, 
                deliver_to= deliver_to
                )
            model.save()
            return redirect('/')
        else:
            messages.error(request, "None of this field can be blank. Please, fill all of them")
            return redirect(f'/books/{ book_id }/neworder')

    return render(request, 'order/new_order.html')
