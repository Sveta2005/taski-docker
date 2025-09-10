"""
Модуль настройки панели администратора для приложения API проекта Taski.

Содержит регистрацию моделей и кастомизацию отображения в Django Admin.
"""

from django.contrib import admin

from .models import Task


class TaskAdmin(admin.ModelAdmin):
    """Настройка отображения модели Task в панели администратора."""

    list_display = (
        'title',
        'description',
        'completed',
    )


# Регистрация модели Task с кастомным админским классом
admin.site.register(Task, TaskAdmin)
