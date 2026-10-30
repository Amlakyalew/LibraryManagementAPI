from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import AuthorViewSet, BookViewSet


router = DefaultRouter()
router.register('authors', viewset=AuthorViewSet)
router.register('books', viewset=BookViewSet)

urlpatterns = router.urls