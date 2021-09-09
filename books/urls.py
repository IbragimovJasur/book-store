from django.urls import path
from .views import (
    BookListView, 
    BookDetailView, 
    BookCreateView, 
    BookUpdateView, 
    SearchResultListView, 
    createreview, 
    deletereview,
    neworder
)

urlpatterns= [
    path('', BookListView.as_view(), name='book_list'),
    path('<uuid:pk>/', BookDetailView.as_view(), name='book_detail'),
    path('createnew/', BookCreateView.as_view(), name='create_book'),
    path('<uuid:pk>/update/', BookUpdateView.as_view(), name='update_book'),
    path('search/', SearchResultListView.as_view(), name='search_result'),
    path('<uuid:book_id>/newcomment/', createreview, name='add_comment'),
    path('<uuid:book_id>/<int:review_id>/delete/', deletereview, name='delete_comment'),
    path('<uuid:book_id>/neworder/', neworder, name='new_order'),
]