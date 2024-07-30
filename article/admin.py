from django.contrib import admin
from .models import Article

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'file1', 'file2', 'file3', 'file4', 'file5', 'ctime', 'click', 'user')

admin.site.register(Article, ArticleAdmin)