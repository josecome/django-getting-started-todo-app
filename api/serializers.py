from rest_framework import serializers
from main.models import (
    TodoItem
)

class TodoItemSerializer(serializers.ModelSerializer):
    class Meta:        
        model = TodoItem
        fields = ["id", "name", "completed", "is_deleted"]