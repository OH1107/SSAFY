# Django의 주요 유효성 검사 도구 중 하나
# 공격이나 우연한 데이터 손상에 대한 방어 수단

from django import forms
from .models import Article


# Markup input을 생성하는 기능
# 사용자 데이터를 받아서 validation 기능
class ArticleForm(forms.ModelForm):
    title = forms.CharField(
        label='제목',
        widget=forms.TextInput(
            attrs={
                'class': 'my-title',
                'placeholder': 'Enter Title',
                'maxlength': 20,
            }
        )
    )

    content = forms.CharField(
        label='내용',
        widget=forms.Textarea(
            attrs={
                'class': 'my-content',
                'placeholder': 'Enter Content',
                'rows': 5,
                'cols': 50,
            }
        ),
        error_messages={
            'required': 'Please enter your content',
        }
    )
    # content

    class Meta:
        model = Article
        fields = '__all__'