from django.contrib import admin
from .models import BookList, Review

class ReviewInline(admin.TabularInline):
    model= Review
    extra= 0

class BookAdmin(admin.ModelAdmin):
    inlines= [
        ReviewInline,
    ]
    list_display= ('title', 'posted_by', 'author', 'price',)

admin.site.register(BookList, BookAdmin)

