import uuid
from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model

class BookList(models.Model):
    id= models.UUIDField(primary_key= True, default= uuid.uuid4, editable= False)
    title= models.CharField(max_length=150)
    author= models.CharField(max_length=150)
    price= models.DecimalField(max_digits=7, decimal_places=2)
    image= models.ImageField(upload_to= 'covers/', blank= True)
    posted_by= models.ForeignKey(get_user_model(), on_delete=models.CASCADE, default='someone')
    date= models.DateTimeField(auto_now_add=True, null=True, blank=True)

    class Meta:
        ordering= ['-date']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('book_detail', args=[str(self.id)])

class Review(models.Model):
    book= models.ForeignKey(BookList, on_delete=models.CASCADE, related_name='reviews')
    sentence= models.CharField(max_length=200)
    author= models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    def __str__(self):
        return self.sentence
