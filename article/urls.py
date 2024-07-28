from django.urls import path
from .views import ArticleListView, ArticleCreateView, ArticleFormView, ArticleUpdateView, ArticleDeleteView, ArticleDetailView

app_name = 'article'
urlpatterns = [
    path('', ArticleListView.as_view(), name='list'),
    path('create', ArticleCreateView.as_view(), name='create'),
    path('create2', ArticleFormView.as_view(), name='create2'),
    path('update/<int:pk>', ArticleUpdateView.as_view(), name='update'),
    path('delete/<int:pk>', ArticleDeleteView.as_view(), name='delete'),
    path('detail/<int:pk>', ArticleDetailView.as_view(), name='detail'),
]