from django.db import models
from django.contrib.auth.models import PermissionsMixin, AbstractBaseUser, BaseUserManager


class CustomAccountManager(BaseUserManager):
    def create_user(self, email, password, first_name, last_name, profession):
        user = self.model(email=email, first_name=first_name, last_name=last_name, profession=profession, password=password)
        user.set_password(password)
        user.is_staff = False
        user.is_superuser = False
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password, first_name, last_name, profession):
        user = self.create_user(email=email, first_name=first_name, last_name=last_name, profession=profession, password=password)
        user.is_active = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    profession = models.CharField(max_length=100)
    is_staff = models.BooleanField(default=False)
    is_aproove = models.BooleanField(default=False)
    REQUIRED_FIELDS = ['first_name', 'last_name', 'profession']
    USERNAME_FIELD = 'email'

    objects = CustomAccountManager()

    def get_short_name(self):
        return self.email

    def natural_key(self):
        return self.email

    def __str__(self):
        return self.email
