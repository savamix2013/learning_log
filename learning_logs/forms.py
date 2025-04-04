from django import forms
from .models import Articles

from .models import Topic, Entry

class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ['text']
        labels = {'text': ''}

class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['text']
        labels = {'text': ''}
        widgets = {'text': forms.Textarea(attrs={'cols': 80})}

class ArticlesForm(forms.ModelForm):
    class Meta:
        model = Articles
        fields = ['title', 'content']
        labels = {'title': 'Заголовок', 'content': 'Контент'}
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Введіть заголовок статті'}),
            'content': forms.Textarea(attrs={'placeholder': 'Введіть текст статті'}),
        }
