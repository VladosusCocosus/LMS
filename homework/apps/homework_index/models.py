from django.db import models
import datetime

from django.utils import timezone

class Article(models.Model):
    homework_author = models.CharField('Автор', max_length=50, default='')
    homework_lesson = models.CharField('Название урока', max_length=100)
    homework = models.TextField('Задание')
    use_date = models.DateField('Дата урока', default='', null=True)
    date_for_server = models.TextField('Дата урока', default='', null=True)
    pub_date = models.DateTimeField('Дата публикации')
