from django import forms
from .models import GuessNumbers

class PostForm(forms.ModelForm):
    
    class Meta:
        model = GuessNumbers
        # 사용자로부터 form을 통해 받아올 데이터를 입력한다.
        fields = ('name', 'text',)