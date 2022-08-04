from rest_framework import serializers
from tasks.models import Tasks


class TaskSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tasks
        fields = (
            'title',
            'description',
            'status',
            'deadline_date',
        )
