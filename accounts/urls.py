from django.urls import path, include
from django.views.generic import TemplateView

from .views import LogoutView, EditProfileView, EmailVerify, RegisterView, MyLoginView

urlpatterns = [
    path('login/', MyLoginView.as_view(), name='login'),
    path('registration/', RegisterView.as_view(), name="registration"),
    path('confirm_email/', TemplateView.as_view(template_name='accounts/confirm_email.html'), name='confirm_email'),
    path('invalid_verify/', TemplateView.as_view(template_name='accounts/invalid_verify.html'), name='invalid_verify'),
    path('verify_email/<uidb64>/<token>/', EmailVerify.as_view(), name='verify_email'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('profile/<int:pk>/', EditProfileView.as_view(), name='profile'),
]

