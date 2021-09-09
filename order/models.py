from django.db import models
from django.contrib.auth import get_user_model
from books.models import BookList

class Order(models.Model):
    ordered_by= models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    book= models.ForeignKey(BookList, on_delete=models.CASCADE, related_name='order_list')
    date_of_order= models.DateTimeField(auto_now_add=False, null=True, blank=True)
    date_of_delivery= models.DateTimeField(auto_now_add=False, null=True, blank=True)
    card_number= models.CharField(max_length=20, null=False, blank=False)
    deliver_to= models.CharField(max_length=50, null=False, blank=False)

    class Meta:
        ordering= ['date_of_order']

    def __str__(self):
        return self.deliver_to
