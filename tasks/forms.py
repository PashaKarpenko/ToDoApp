from django import forms
from .models import Tasks


class TaskCreateForm(forms.ModelForm):
    PRIORITY = [('Низький', 'Низький'), ('Середній', 'Середній'), ('Високий', 'Високий')]
    IMPORTANCE = [('Низька', 'Низька'), ('Середня', 'Середня'), ('Висока', 'Висока')]

    title = forms.CharField(label="Назва")
    description = forms.CharField(widget=forms.Textarea, label="Повний текст")
    deadline_date = forms.CharField(widget=forms.SelectDateWidget, label="Дата дедлайну")
    priority = forms.ChoiceField(choices=PRIORITY, label="Пріоритет")
    importance = forms.BooleanField(label="Важливість", help_text='Якщо задача важлива поставте відмітку в чекбоксі.')

    class Meta:
        model = Tasks
        fields = ('title', 'description', 'deadline_date', 'priority', 'importance')
