from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

class Article(models.Model):
    title = models.CharField(max_length=100, verbose_name='title', help_text='news title')
    content = models.TextField(verbose_name='content', help_text='news content')
    ctime = models.DateTimeField(auto_now = True)
    click = models.IntegerField(default=0)
    file = models.FileField(upload_to = "upload/", null=True, blank=True)