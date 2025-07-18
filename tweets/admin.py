from django.contrib import admin

from tweets.models import Book, Movies

# Register your models here.
admin.site.register(Book)
admin.site.register(Movies)