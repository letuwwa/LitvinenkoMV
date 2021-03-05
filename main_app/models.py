from django.db import models
from django.urls import reverse
from django.utils import timezone
from django_currentuser.db.models import CurrentUserField
from django_currentuser.middleware import get_current_authenticated_user


class Feedback(models.Model):
    name = models.CharField(max_length=32, blank=False, verbose_name='Имя')
    text = models.TextField(max_length=1024, blank=False, verbose_name='Текст')
    email = models.EmailField(max_length=256, blank=False, verbose_name='Почта для ответа')
    date = models.DateTimeField(default=timezone.now, blank=False)


JOB_TYPE = (
    ('Part Time', 'Part Time'),
    ('Full Time', 'Full Time'),
    ('Freelance', 'Freelancer'),
)


class JobModel(models.Model):
    user = CurrentUserField(default=get_current_authenticated_user, blank=True, editable=False)
    title = models.CharField(max_length=100, blank=False, verbose_name='Название вакансии')
    company_name = models.CharField(max_length=200, blank=False, verbose_name='Название компании')
    employment_status = models.CharField(choices=JOB_TYPE, max_length=10, verbose_name='Занятость')
    description = models.TextField(verbose_name='Описание')
    responsibilities = models.TextField(verbose_name='Задачи')
    experience = models.CharField(max_length=100, verbose_name='Навыки')
    job_location = models.CharField(max_length=120, verbose_name='Местоположение')
    salary = models.CharField(max_length=100, null=True, blank=True, verbose_name='ЗП')
    published_on = models.DateTimeField(default=timezone.now, blank=False, verbose_name='Дата публикации')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("job_single", args=[self.id])


APPLY_STATUS = (
    ('Отправлен', 'Отправлен'),
    ('Отказ', 'Отказ'),
    ('Вас пригласили', 'Вас пригласили'),
)


class JobApplyModel(models.Model):
    user = CurrentUserField(default=get_current_authenticated_user, blank=False, editable=False, verbose_name='Пользователь', null=True)
    job = models.ForeignKey('JobModel', on_delete=models.CASCADE, blank=False, verbose_name='Вакансия')
    status = models.CharField(max_length=32, choices=APPLY_STATUS, default='Отправлен', verbose_name='Статус')
    apply_request = models.TextField(verbose_name='Сопроводительное письмо')
    apply_response = models.TextField(verbose_name='Ответ')
    apply_published_date = models.DateTimeField(default=timezone.now, blank=False)

    def __str__(self):
        return 'Отклик на ' + self.job.title

    def get_absolute_url(self):
        return reverse('response_single', args=[self.id])

    class Meta:
        ordering = ["-apply_published_date"]