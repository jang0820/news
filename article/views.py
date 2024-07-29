from django.views.generic import FormView, ListView, CreateView, UpdateView, DeleteView, DetailView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect, HttpResponse, FileResponse, Http404
import os
from .models import Article
from .forms import ArticleModelForm



class ArticleListView(ListView):
    model = Article
    queryset = Article.objects.all() 
    template_name = 'article_list.html'  # 樣板路徑

class ArticleCreateView(CreateView): #使用CreateView寫入資料到資料庫
    model = Article  #指定資料表
    form_class = ArticleModelForm  # 使用的表單類別
    template_name = 'article_create.html' # 樣板
    success_url = '/article'  # 儲存成功後要導向的網址

    def form_valid(self, form):
        form.instance.user = self.request.user  #資料表內的user來自於self.request.user
        return super(ArticleCreateView, self).form_valid(form) #寫入資料庫

    @method_decorator(login_required)  #需要登入才能使用，修飾dispatch
    def dispatch(self, request, *arg, **kwargs):
        if (request.user.has_perm('article.article_create')): #需要權限news.news_create
            return super().dispatch(request, *arg, **kwargs)
        else:
            raise Http404()

class ArticleUpdateView(LoginRequiredMixin, UpdateView):
    login_url = '/accounts/login/'
    model = Article
    form_class = ArticleModelForm  # 使用的表單類別
    template_name = 'article_update.html'  # 修改樣板
    success_url = '/article'  # 儲存成功後要導向的網址

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        article = Article.objects.filter(pk = self.kwargs.get("pk"))  #updatenews為QuerySet物件，每個元素都是News
        context['article'] = article[0]   #增加變數到context
        return context
    
    def get(self, request, *args, **kwargs):
        a = Article.objects.filter(pk = self.kwargs.get("pk"))
        if ((a[0].user == request.user and request.user.has_perm('article.article_update')) or request.user.is_superuser):
            return super().get(request, *args, **kwargs)
        else:
            raise Http404()

class ArticleDeleteView(DeleteView):
    model = Article
    template_name = 'article_delete.html'  # 刪除樣板
    success_url = '/article'  # 刪除成功後要導向的網址

    def form_valid(self, form): #DeleteView的form，呼叫post函式，接著呼叫form_valid後刪除元素
        article = Article.objects.filter(pk=self.kwargs.get("pk"))
        a = article[0]
        if a.file != "":
            os.remove('{}'.format(a.file))  # 刪除檔案
        return super(ArticleDeleteView, self).form_valid(form)

class ArticleDetailView(DetailView):
    model = Article
    template_name = 'article_detail.html'

    def get(self, request, *arg, **kwargs):
        item = Article.objects.get(pk = self.kwargs.get("pk"))  #GET網頁時，更新點擊次數
        item.click = item.click+1
        item.save()
        return super().get(request, *arg, **kwargs)