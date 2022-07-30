from django import forms
from .models import Tasks


class TaskCreateForm(forms.ModelForm):
    PRIORITY = [('Низький', 'Низький'), ('Середній', 'Середній'), ('Високий', 'Високий')]
    IMPORTANCE = [('Низька', 'Низька'), ('Середня', 'Середня'), ('Висока', 'Висока')]

    title = forms.CharField(label="Назва")
    description = forms.CharField(widget=forms.Textarea, label="Повний текст")
    deadline_date = forms.CharField(label="Дата дедлайну")
    priority = forms.ChoiceField(choices=PRIORITY, label="Пріоритет")
    importance = forms.ChoiceField(choices=IMPORTANCE, label="Важливість")

    class Meta:
        model = Tasks
        fields = ('title', 'description', 'deadline_date', 'priority', 'importance')
