from django import forms
from .models import Article

class ArticleModelForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ('title', 'content','file1','file2','file3','file4','file5')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '標題'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'placeholder': '內容'}),
            'file1': forms.FileInput(attrs={'class': 'form-control', 'placeholder': '上傳附件1'}),
            'file2': forms.FileInput(attrs={'class': 'form-control', 'placeholder': '上傳附件2'}),
            'file3': forms.FileInput(attrs={'class': 'form-control', 'placeholder': '上傳附件3'}),
            'file4': forms.FileInput(attrs={'class': 'form-control', 'placeholder': '上傳附件4'}),
            'file5': forms.FileInput(attrs={'class': 'form-control', 'placeholder': '上傳附件5'}),
        }
