# -*- coding:utf-8 -*-
from django.utils import timezone
from django.conf import settings
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericRelation
from django.db import models
import datetime


class Like(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             related_name='likes',
                             on_delete=models.CASCADE)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')
    couner = models.IntegerField()


class Post(models.Model):
    title = models.CharField(max_length = 200)
    text = models.TextField()
    create_date = models.DateTimeField(default=timezone.now)
    city = models.CharField(max_length = 32)
    image = models.ImageField(upload_to = './', null = True)
    likes = GenericRelation(Like)
    #dislikes = models.IntegerField()
    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
    def __str__ (self):
        return self.title

    @property
    def total_likes(self):
        return self.likes.count()

class Question(models.Model):
    """Вопрос"""
    Post_id = models.ForeignKey(Post,on_delete=models.CASCADE)
    title = models.CharField(max_length=200, verbose_name = "Вопрос")
    date_published = models.DateTimeField(verbose_name = "Дата публикации",
        default = datetime.datetime.now())
    is_active = models.BooleanField(verbose_name = "Опубликован")

    def __str__(self):
        return self.title


    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'


class Answer(models.Model):
    """Вариант ответа на вопрос"""
    question_id = models.ForeignKey(Question,on_delete=models.CASCADE)
    answer = models.CharField(max_length=200, verbose_name = "Ответ")
    votes = models.IntegerField(verbose_name = "Голосов", default = 0)

    def __str__(self):
        return self.answer

    class Meta:
        verbose_name = 'Ответ'
        verbose_name_plural = 'Ответы'
