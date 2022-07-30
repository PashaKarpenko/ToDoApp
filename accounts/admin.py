from django.contrib import admin
from .models import CustomUser


class UsersAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name')
    list_filter = ['first_name', 'last_name']
    list = ('first_name', 'last_name')

    class Meta:
        model = CustomUser


admin.site.register(CustomUser, UsersAdmin)


