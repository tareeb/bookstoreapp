from django.contrib import admin
from .models import User, Writer, Book, Testimonial, Review, Comment, Favorite , Order

# Register your models here.

class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'username', 'password')

admin.site.register(User)

class WriterAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

admin.site.register(Writer)

class BookAdmin(admin.ModelAdmin):
    list_display = ('id', 'price', 'name', 'writer' , 'image_url')
    
admin.site.register(Book)

class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'text')
    
admin.site.register(Testimonial)

class ReviewAdmin(admin.ModelAdmin):
    list_display = ('id', 'text', 'user', 'book')
    
admin.site.register(Review)

class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'text', 'review', 'user')
    
admin.site.register(Comment)

class FavoriteAdmin(admin.ModelAdmin):
    list_display = ('id', 'book', 'user')
    
admin.site.register(Favorite)


class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'book', 'total_price', 'date')
    
admin.site.register(Order)