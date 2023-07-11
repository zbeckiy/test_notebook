from datetime import datetime

from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    category_name = models.CharField(max_length=150)

    def __str__(self):
        return self.category_name


class Note(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=150, verbose_name="Заголовок")
    content = models.TextField(verbose_name="Содержимое", null=True, default="")
    datetime_created = models.DateTimeField(default=datetime.now(), verbose_name="Дата создания")
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, verbose_name="Тип записи", null=True,)
    is_favorite = models.BooleanField(verbose_name="Избранное", default=False)
    note_uuid = models.UUIDField(null=True, blank=True)
    is_accessible_by_uuid = models.BooleanField(default=False)

    def __str__(self):
        return self.title
