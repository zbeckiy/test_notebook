# Generated by Django 4.2.3 on 2023-07-10 17:50

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='Заголовок')),
                ('content', models.TextField(default='', null=True, verbose_name='Содержимое')),
                ('datetime_created', models.DateTimeField(default=datetime.datetime(2023, 7, 10, 20, 50, 25, 999550), verbose_name='Дата создания')),
                ('is_favorite', models.BooleanField(default=False, verbose_name='Избранное')),
                ('note_uuid', models.UUIDField(blank=True, null=True)),
                ('is_accessible_by_uuid', models.BooleanField(default=False)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='notes.category', verbose_name='Тип записи')),
            ],
        ),
    ]
