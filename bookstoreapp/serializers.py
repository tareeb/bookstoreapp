from rest_framework import serializers
from .models import User, Writer, Book, Testimonial, Review, Comment, Favorite

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'name', 'email', 'password']

class BookSerializer(serializers.ModelSerializer):
    writer_name = serializers.CharField(source='writer.name', read_only=True)

    class Meta:
        model = Book
        fields = ['id', 'price', 'name', 'writer', 'writer_name' , 'image_url']

class WriterSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Writer
        fields = ['id', 'name']

class TestimonialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Testimonial
        fields = ['id', 'user', 'text']

class ReviewSerializer(serializers.ModelSerializer):
    username = serializers.SerializerMethodField()
    bookname = serializers.SerializerMethodField()

    class Meta:
        model = Review
        fields = ['id', 'text', 'user', 'book', 'username', 'bookname']

    def get_username(self, obj):
        return obj.user.name

    def get_bookname(self, obj):
        return obj.book.name

class CommentSerializer(serializers.ModelSerializer):
    username = serializers.SerializerMethodField()
    
    class Meta:
        model = Comment
        fields = ['id', 'text', 'review', 'user' , 'username']
        
    def get_username(self, obj):
        return obj.user.name

class FavoriteSerializer(serializers.ModelSerializer):
    bookname = serializers.SerializerMethodField()

    class Meta:
        model = Favorite
        fields = ['id', 'book', 'user', 'bookname']

    def get_username(self, obj):
        return obj.user.name

    def get_bookname(self, obj):
        return obj.book.name
