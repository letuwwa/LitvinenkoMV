from django.conf import settings
from django.db import models
from django.urls import reverse
from django.utils import timezone


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
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, editable=False, blank=True)
    title = models.CharField(max_length=100, blank=False)
    company_name = models.CharField(max_length=200, blank=False)
    employment_status = models.CharField(choices=JOB_TYPE, max_length=10)
    description = models.TextField()
    responsibilities = models.TextField()
    experience = models.CharField(max_length=100)
    job_location = models.CharField(max_length=120)
    salary = models.CharField(max_length=100, null=True, blank=True)
    published_on = models.DateTimeField(default=timezone.now, blank=False)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("job_single", args=[self.id])
