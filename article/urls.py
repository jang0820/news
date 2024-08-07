from django.urls import path
from .views import ArticleListView, ArticleCreateView, ArticleUpdateView, ArticleDeleteView, ArticleDetailView, downloadFile

app_name = 'article'
urlpatterns = [
    path('', ArticleListView.as_view(), name='list'),
    path('create', ArticleCreateView.as_view(), name='create'),
    path('update/<int:pk>', ArticleUpdateView.as_view(), name='update'),
    path('delete/<int:pk>', ArticleDeleteView.as_view(), name='delete'),
    path('detail/<int:pk>', ArticleDetailView.as_view(), name='detail'),
    path('download/(?P<filepath>.*)/$', downloadFile, name='download'),
]