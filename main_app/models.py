from django.db import models
from django.utils import timezone


class Feedback(models.Model):
    name = models.CharField(max_length=32, blank=False, verbose_name='Имя')
    text = models.TextField(max_length=1024, blank=False, verbose_name='Текст')
    email = models.EmailField(max_length=256, blank=False, verbose_name='Почта для ответа')
    date = models.DateTimeField(default=timezone.now, blank=False)
