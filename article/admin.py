from django.contrib import admin
from .models import Article

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'file', 'ctime', 'click', 'user')

admin.site.register(Article, ArticleAdmin)