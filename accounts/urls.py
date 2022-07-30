from django.urls import path
from .views import RegisterFormView, LoginFormView, LogoutView, EditProfileView

urlpatterns = [
    path('registration/', RegisterFormView.as_view(), name="registration"),
    path('login/', LoginFormView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('profile/<int:pk>/', EditProfileView.as_view(), name='profile')

]
