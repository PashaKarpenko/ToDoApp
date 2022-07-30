from .forms import UserCreateForm, EditUserDataForm
from .models import CustomUser
from django.urls import reverse_lazy, reverse
from django.views.generic import FormView
from django.views.generic.edit import UpdateView
from django.views import View
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import redirect


class RegisterFormView(FormView):
    form_class = UserCreateForm
    success_url = reverse_lazy("registration")
    template_name = "accounts/registration.html"

    def form_valid(self, form):
        form.save()
        email = self.request.POST['email']
        password = self.request.POST['password1']
        user = authenticate(email=email, password=password)
        login(self.request, user)
        return super().form_valid(form)


class LoginFormView(FormView):
    form_class = AuthenticationForm
    template_name = "accounts/login.html"
    success_url = reverse_lazy("all_tasks")
    print('authenticated')

    def form_valid(self, form):
        self.user = form.get_user()
        login(self.request, self.user)
        return super().form_valid(form)


class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect(reverse('registration'))


class EditProfileView(UpdateView):
    model = CustomUser
    form_class = EditUserDataForm
    success_url = reverse_lazy("all_tasks")
    template_name = 'accounts/profile.html'

