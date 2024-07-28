from django import forms
from .models import Article

class ArticleModelForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ('title', 'content','file')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '標題'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'placeholder': '內容'}),
            'file': forms.FileInput(attrs={'class': 'form-control', 'placeholder': '上傳附件'}),
        }
