from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model


class UserCreateForm(UserCreationForm):
    email = forms.EmailField(label="Email")
    first_name = forms.CharField(label="Ім'я")
    last_name = forms.CharField(label="Прізвище")
    profession = forms.CharField(label="Професія")

    class Meta:
        model = get_user_model()
        fields = ('email', 'first_name', 'last_name', 'profession', 'password1', 'password2')

    def save(self, commit=True):
        user = super(UserCreateForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.profession = self.cleaned_data['profession']
        if commit:
            user.save()
        return user


class EditUserDataForm(forms.ModelForm):
    first_name = forms.CharField(label="Ім'я")
    last_name = forms.CharField(label="Прізвище")
    profession = forms.CharField(label="Професія")

    class Meta:
        model = get_user_model()
        fields = ('first_name', 'last_name', 'profession')

    def save(self, commit=True):
        user = super(EditUserDataForm, self).save(commit=False)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.profession = self.cleaned_data['profession']
        if commit:
            user.save()
        return user