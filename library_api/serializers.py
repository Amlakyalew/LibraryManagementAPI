from rest_framework import serializers
from django.db.models import F
from .models import Author, Book


class AuthorSerializer(serializers.ModelSerializer):
    books = serializers.StringRelatedField(many=True, read_only=True)
    
    class Meta:
        model = Author
        fields = ['id', 'first_name', 'last_name', 'bio', 'date_of_birth', 'created_at', 'books']



class CustomAuthorSerializer(serializers.ModelSerializer):
    full_name = serializers.SerializerMethodField()

    def get_full_name(self, author):
        return f"{author.first_name} {author.last_name}"

    class Meta:
        model = Author
        fields = ['id', 'full_name', 'bio', 'date_of_birth']



class BookSerializer(serializers.ModelSerializer):
    author = CustomAuthorSerializer(read_only=True)
    author_id = serializers.PrimaryKeyRelatedField(
        queryset = Author.objects.all(),
        # slug_field = 'first_name',
        source = 'author',
        write_only = True,
        required = False
        )
    
    class Meta:
        model = Book
        fields = ['id', 'title', 'author', 'author_id', 'isbn', 'genre', 'published_date', 'available']