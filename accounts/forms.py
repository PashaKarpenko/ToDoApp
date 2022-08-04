from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import get_user_model, authenticate
from django.core.exceptions import ValidationError
from accounts.utils import send_email_for_verify


class MyAuthenticationForm(AuthenticationForm):

    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        if username is not None and password:
            self.user_cache = authenticate(
                self.request,
                username=username,
                password=password,
            )
            if not self.user_cache.is_verified:
                send_email_for_verify(self.request, self.user_cache)
                raise ValidationError(
                    'Email не підтверджений, перевірте будь ласка пошту',
                    code='invalid_login',
                )
            if self.user_cache is None:
                raise self.get_invalid_login_error()
            else:
                self.confirm_login_allowed(self.user_cache)
        return self.cleaned_data


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
