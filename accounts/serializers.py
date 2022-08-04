from rest_framework import serializers
from accounts.models import CustomUser


class EditUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomUser
        fields = (
            'email',
            'first_name',
            'last_name',
            'is_verified',
            'profession',
        )
