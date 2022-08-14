from django.contrib.auth.views import LoginView
from django.core.exceptions import ValidationError
from django.utils.http import urlsafe_base64_decode
from .forms import UserCreateForm, EditUserDataForm, MyAuthenticationForm
from .models import CustomUser
from django.urls import reverse_lazy, reverse
from django.views.generic.edit import UpdateView
from django.views import View
from django.contrib.auth import login, logout, authenticate, get_user_model
from django.shortcuts import redirect, render
from django.contrib.auth.tokens import default_token_generator as token_generator
from .utils import send_email_for_verify


User = get_user_model()


class MyLoginView(LoginView):
    form_class = MyAuthenticationForm
    template_name = "accounts/login.html"
    next_page = "all_tasks"
    redirect_authenticated_user = "all_tasks"


class RegisterView(View):
    def get(self, request):
        context = {
            'form': UserCreateForm()
        }
        return render(request, 'accounts/registration.html', context)

    def post(self, request):
        form = UserCreateForm(request.POST)

        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password1')
            user = authenticate(email=email, password=password)
            send_email_for_verify(request, user)
            return redirect('confirm_email')
        context = {
            'form': form
        }
        return render(request, 'accounts/registration.html', context)


class EmailVerify(View):
    def get(self, request, uidb64, token):
        user = self.get_user(uidb64)

        if user is not None and token_generator.check_token(user, token):
            user.is_verified = True
            user.save()
            login(request, user)
            return redirect('all_tasks')
        return redirect('invalid_verify')

    @staticmethod
    def get_user(uidb64):
        try:
            uid = urlsafe_base64_decode(uidb64).decode()
            user = User.objects.get(pk=uid)
        except (TypeError, ValueError, OverflowError,
                User.DoesNotExist, ValidationError):
            user = None
        return user


class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect(reverse('login'))


class EditProfileView(UpdateView):
    model = CustomUser
    form_class = EditUserDataForm
    success_url = reverse_lazy("all_tasks")
    template_name = 'accounts/profile.html'
