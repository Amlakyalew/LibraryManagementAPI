from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import Author, Book
from .serializers import AuthorSerializer, BookSerializer


class AuthorViewSet(ModelViewSet):
    http_method_names = ['head', 'options', 'get', 'post', 'patch', 'delete']

    # def get_permissions(self):
    #     if self.request.method in ['POST', 'PATCH', 'DELETE']:
    #         return [IsAuthenticated()]
    #     return [AllowAny()]
    
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class BookViewSet(ModelViewSet):
    http_method_names = ['head', 'options', 'get', 'post', 'patch', 'delete']
    
    # def get_permissions(self):
    #     if self.request.method in ['POST', 'PATCH', 'DELETE']:
    #         return [IsAuthenticated()]
    #     return [AllowAny()]
    
    queryset = Book.objects.all()
    serializer_class = BookSerializer
