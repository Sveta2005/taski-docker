"""Модуль с моделями проекта Taski."""

from django.db import models


class Task(models.Model):
    """Модель Task для хранения информации о задачах."""

    title = models.CharField(verbose_name='Заголовок', max_length=120)
    description = models.TextField()
    completed = models.BooleanField(default=False)

    def __str__(self):
        """Возвращает строковое представление задачи (title)."""
        return self.title
