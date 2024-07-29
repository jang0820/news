from django.db import models
from django.conf import settings

class Article(models.Model):
    title = models.CharField(max_length=100, verbose_name='title', help_text='news title')
    content = models.TextField(verbose_name='content', help_text='news content')
    ctime = models.DateTimeField(auto_now = True)
    click = models.IntegerField(default=0)
    file = models.FileField(upload_to = "upload/", null=True, blank=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='news_user', null = True)

    def __str__(self):
        return self.title

    class Meta:
        permissions = (
            ("article_delete", "Can Delete Article"),
            ("article_create", "Can Create Article"),
            ("article_update", "Can Update Article"),
        )