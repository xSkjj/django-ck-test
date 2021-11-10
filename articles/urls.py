from .views import ArticleListView, ArticleDetailView, landing
from django.urls import path

urlpatterns = [
    path('list/', ArticleListView.as_view(), name='article-list'),
    path('detail/<int:pk>/', ArticleDetailView.as_view(), name='article-detail'),
    path('', landing)
]
