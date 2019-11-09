# -*- coding:utf-8 -*-
from django.conf import settings
from django.db import models
from django.utils import timezone
import datetime


class Post(models.Model):
    title = models.CharField(max_length = 200)
    text = models.TextField()
    create_date = models.DateTimeField(default=timezone.now)
						#Место откуда фото качаются
#    image = models.ImageField(upload_to = '/',height_field = 100, Width_field = 100)
    up = models.IntegerField()
    dis = models.IntegerField()
    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
    def __str__ (self):
        return Post


class Question(models.Model):
    """Вопрос"""
    
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
