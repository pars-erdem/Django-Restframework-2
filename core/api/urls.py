from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views as api_views

router = DefaultRouter()
router.register(r'publishers', api_views.PublisherViewSet)
router.register(r'authors', api_views.AuthorViewSet)
router.register(r'categories', api_views.CategoryViewSet)
router.register(r'books', api_views.BookViewSet)
router.register(r'reviewers', api_views.ReviewerViewSet)
router.register(r'reviews', api_views.ReviewViewSet)
urlpatterns = [
    path('', include(router.urls)),
]
