"""Модуль сериализаторов приложения API проекта Taski."""

from rest_framework import serializers
from .models import Task


class TaskSerializer(serializers.ModelSerializer):
    """Сериализатор для модели Task."""

    class Meta:
        """Мета-класс, описывающий модель и поля для сериализации."""

        model = Task
        fields = (
            'id',
            'title',
            'description',
            'completed',
        )
